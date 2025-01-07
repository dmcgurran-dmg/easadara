import json
import sys

from createhypertables import create_tables
from gettableaudata import get_catalog_data
from outputtohyper import write_catalog_to_hyper
from getrepositorydata import get_and_write_repo_data_to_hyper

import tableauhyperapi
import tableauserverclient as TSC
from tableauhyperapi import HyperProcess, Telemetry, CreateMode, Connection
from datetime import datetime


# Colors used in console prints
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[42m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CONSOLE_SPACER = '  '


class SuperServer(TSC.Server):
    def __init__(self, *args, **kwargs):
        super(SuperServer, self).__init__(*args, **kwargs)
        self.header = None


def get_sites(tab_server):
    request_options = TSC.RequestOptions(pagesize=1000)
    sites = list(TSC.Pager(tab_server.sites, request_options))

    return sites


def authenticate_with_ts(loaded_settings, tableau_server_type):
    # Get access credentials
    server_url = loaded_settings['TS_SERVER_URL']
    pat_name = loaded_settings['PAT_NAME']
    pat = loaded_settings['PAT_SECRET']
    site_id = loaded_settings['SITE_ID']

    # Print the status to the console
    if tableau_server_type == "on_prem":
        print('{0}Attempting to login to Tableau Server - {1} ...{2}'.format(bcolors.WARNING, server_url, bcolors.ENDC))
    elif tableau_server_type == "cloud":
        print('{0}Attempting to login to Tableau Cloud Pod - {1} ...{2}'.format(bcolors.WARNING, server_url,
                                                                                bcolors.ENDC))
        print(
            '{0}Attempting to login to Tableau Cloud Site - {1} ...{2}'.format(bcolors.WARNING, site_id, bcolors.ENDC))

    # Make sure we use an updated version of the rest api
    tab_server = SuperServer(server_url, use_server_version=True)

    # Attempt to authenticate using personal access token
    tableau_auth = TSC.PersonalAccessTokenAuth(token_name=pat_name, personal_access_token=pat)

    # Connect to the site specified
    tableau_auth.site_id = ""
    if tableau_server_type == "on_prem":
        tableau_auth.site_id = ""
    elif tableau_server_type == "cloud":
        tableau_auth.site_id = site_id

    # Sign in with the personal access token
    tab_server.auth.sign_in_with_personal_access_token(tableau_auth)

    # Set the headers we will use on subsequent calls to the API
    tab_server.header = {'Accept': 'application/json;charset=utf-8', 'content-type': 'application/json;charset=utf-8',
                         'X-Tableau-Auth': tab_server.auth_token}

    # Print the status to the console
    print('{0}{1}Successfully logged in!{2}'.format(bcolors.CONSOLE_SPACER, bcolors.OKGREEN, bcolors.ENDC))

    # Return the server
    return tab_server, tableau_auth


# This function reads in credentials from a file to be used by all the scripts
def read_in_settings():
    # Print the status to the console
    print(bcolors.CONSOLE_SPACER + bcolors.WARNING + 'Attempting to read in the Credentials' + bcolors.ENDC)

    # Open up the credentials file
    with open('data/settings.json') as settings_file:
        # Read in the credentials
        read_settings = json.load(settings_file)

    # Return the credentials
    return read_settings


if __name__ == '__main__':
    # Record when we start
    start = datetime.now().time()

    # Read in the settings
    settings = read_in_settings()
    server_type = settings["SERVER_TYPE"]
    output_file = settings["HYPER_OUTPUT"]
    visualize_mode = settings["VISUALIZE_MODE"]
    extract_schema = settings["EXTRACT_SCHEMA"]
    include_exclude_flag = settings["INCLUDE_EXCLUDE_FLAG"]
    site_list = settings["SITE_LIST"]

    try:
        relogin_on_change_site = eval(settings["RELOGIN_ON_CHANGE_SITE"])
    except Exception as e:
        relogin_on_change_site = False
        print("RELOGIN_ON_CHANGE_SITE value should be 'True' or 'False'\nDefault value of 'False' used\n", format(e))

    try:
        abort_on_error_value = eval(settings["ABORT_ON_ERROR"])
    except Exception as e:
        abort_on_error_value = False
        print("ABORT_ON_ERROR value should be 'True' or 'False'\nDefault value of 'False' used\n", format(e))

    # If Cloud Server then no repo tables
    if server_type == "cloud":
        visualize_mode = "catalog"

    # Log into Tableau Server
    server, authentication_token = authenticate_with_ts(settings, server_type)
    all_sites = None
    selected_sites = []
    if server_type == "on_prem":
        all_sites = get_sites(server)
        if include_exclude_flag == "INCLUDE" or include_exclude_flag == "EXCLUDE":
            # We are not looking for all sites
            for current_site in all_sites:
                if include_exclude_flag == "INCLUDE":
                    # Just select the sites in this list
                    if current_site.name in site_list:
                        selected_sites.append(current_site)
                elif include_exclude_flag == "EXCLUDE":
                    # Exclude the sites in this list
                    if current_site.name not in site_list:
                        # this is an Exclude therefore we need to see if the site is not in the site_list
                        selected_sites.append(current_site)
        else:
            selected_sites = get_sites(server)
        # Limit to just 4 sites
        all_sites = all_sites[0:4]

    if not selected_sites:
        # no sites selected, do not bother with anything else
        print("No sites included or all sites excluded. We will stop here. \n")
    else:
        try:
            # Starts the Hyper Process with telemetry enabled to send data to Tableau.
            # To opt out, simply set telemetry=Telemetry.DO_NOT_SEND_USAGE_DATA_TO_TABLEAU.
            print("Starting Hyper process.")
            with HyperProcess(Telemetry.SEND_USAGE_DATA_TO_TABLEAU) as hyper:
                # Replaces file with CreateMode.CREATE_AND_REPLACE if it already exists.
                print("Opening connection to Hyper file.")
                with Connection(endpoint=hyper.endpoint, database=output_file,
                                create_mode=CreateMode.CREATE_AND_REPLACE) as connection:
                    # Create the schema
                    connection.catalog.create_schema(extract_schema)
                    dict_table_definitions = create_tables(connection, extract_schema, visualize_mode)

                    if visualize_mode == "all" or visualize_mode == "catalog":
                        if server_type == "on_prem":
                            for site in all_sites:
                                print("\nSite Name : {0} - {1}\n".format(site.name, datetime.now().time()))
                                if relogin_on_change_site:
                                    # need to re-login to each site (This is necessary if each log in session is short
                                    # sign out of current session
                                    server.auth.sign_out()
                                    print("Signing out")
                                    # sign back in
                                    server.auth.sign_in(authentication_token)
                                    print("Signing in")
                                    auth_token = server.auth.switch_site(site)
                                else:
                                    # No need to re-login, just switch site
                                    print("No need to login or change site")
                                    auth_token = server.auth.switch_site(site)
                                dict_catalog_data = get_catalog_data(TSC, server, authentication_token,
                                                                     abort_on_error_value)
                                write_catalog_to_hyper(server, connection, dict_table_definitions,
                                                       dict_catalog_data)
                        elif server_type == "cloud":
                            dict_catalog_data = get_catalog_data(TSC, server, authentication_token,
                                                                 abort_on_error_value)
                            write_catalog_to_hyper(server, connection, dict_table_definitions, dict_catalog_data)
                    if server_type == "on_prem":
                        if visualize_mode == "all" or visualize_mode == "repo":
                            try:
                                get_and_write_repo_data_to_hyper(connection, dict_table_definitions, settings)
                            except Exception as repo_error:
                                print(repo_error)

                    connection.close()
                    print("The connection to the Hyper file has been closed.\n")
            hyper.shutdown()
            print('The Hyper process has been shut down.\n')

        except tableauhyperapi.HyperException as e:
            sys.exit(e)

    # We are done
    end = datetime.now().time()
    print("Start Time - {0}\nEnd Time - {1}".format(start, end))
