# Queries
SITES_QUERY = "{tableauSites { id, luid, name, uri } }"
DATABASE_QUERY = 'query PagedFieldsQuery($afterToken: String) {databasesConnection(first:1000, after: $afterToken){ ' \
                 'nodes {id, luid, vizportalId, name, description, __typename, connectionType, isCertified, isGrouped, ' \
                 'isControlledPermissionsEnabled, hasActiveWarning, contact{ id, name, email, username, domain, uri}, ' \
                 'downstreamFlows{ id, name, projectName}, downstreamWorkbooks{ id, name, projectName}, ' \
                 'downstreamDatasources{ id, name, projectName}, downstreamMetrics{ id, name, projectName},' \
                 'downstreamLenses{ id, name}, downstreamVirtualConnections{ id, name, projectName},' \
                 '... on DatabaseServer{ hostName, port, extendedConnectionType, service}, ... on File{ filePath}, ' \
                 '... on CloudFile{ provider, fileId, fileExtension, mimeType, requestUrl}, ' \
                 '... on WebDataConnector{ isEmbedded, connectorUrl}}, ' \
                 'pageInfo{ endCursor, hasNextPage}, totalCount}} '
TABLE_QUERY1 = 'query PagedFieldsQuery($afterToken: String) {tablesConnection(first:1000, after: $afterToken) ' \
              '{nodes { id, name, __typename, description, isEmbedded ... on DatabaseTable{ luid, vizportalId, ' \
              'schema, fullName, connectionType, contact { id, name, email, username, domain, uri}, isCertified, ' \
              'database { id, name}, hasActiveWarning, }, ' \
              '... on CustomSQLTable{ query, isUnsupportedCustomSql, tables{id}, database{ id, connectionType, name}}, ' \
              '... on VirtualConnectionTable{ luid, vizportalUrlId, uri, isExtracted, hasActiveWarning, ' \
              'virtualConnection{ id}, extractLastRefreshedAt, extractLastRefreshType, isCertified, owner{ id, name, ' \
              'email, username, domain, uri}}' \
              'downstreamFlows{ id, name, projectName}, downstreamWorkbooks{ id, name, projectName}, ' \
              'downstreamDatasources{ id, name, projectName}, downstreamMetrics{ id, name, projectName},' \
              'downstreamLenses{ id, name}, downstreamVirtualConnections{ id, name, projectName}' \
              '}, ' \
              'pageInfo { endCursor, hasNextPage}, totalCount}} '
TABLE_QUERY = 'query PagedFieldsQuery($afterToken: String) {tablesConnection(first:1000, after: $afterToken) ' \
              '{nodes { id, name, __typename, description, isEmbedded ... on DatabaseTable{ luid, vizportalId, ' \
              'schema, fullName, connectionType, contact { id, name, email, username, domain, uri}, isCertified, ' \
              'database { id, name}, hasActiveWarning, }, ' \
              '... on CustomSQLTable{ query, isUnsupportedCustomSql, tables{id}, database{ id, connectionType, name}}, ' \
              'downstreamFlows{ id, name, projectName}, downstreamWorkbooks{ id, name, projectName}, ' \
              'downstreamDatasources{ id, name, projectName}, downstreamMetrics{ id, name, projectName},' \
              'downstreamLenses{ id, name}, downstreamVirtualConnections{ id, name, projectName}' \
              '}, ' \
              'pageInfo { endCursor, hasNextPage}, totalCount}} '
VCONN_QUERY = 'query PagedFieldsQuery($afterToken: String) {virtualConnectionsConnection(first:1000, after: $afterToken) ' \
              '{nodes { id, name, __typename, luid, projectName, projectVizportalUrlId, containerType, containerName, ' \
              'vizportalId, vizportalUrlId, uri, connectionType, description, owner{ id, name, email, username}, ' \
              'hasActiveWarning, isCertified, createdAt, updatedAt}, ' \
              'pageInfo { endCursor, hasNextPage}, totalCount}} '
COLUMN_QUERY1 = 'query PagedFieldsQuery($afterToken: String) {columnsConnection(first:1000, after: $afterToken){ nodes' \
               ' {id, vizportalId, luid, name, description, descriptionInherited{ assetId}, remoteType, isNullable, ' \
               'table { id, name, __typename, ... on DatabaseTable{ isCertified, database{ id, name, connectionType, ' \
               'isCertified, __typename }}}, downstreamFlows{ id, name, projectName}, downstreamWorkbooks{ id, name, ' \
               'projectName}, downstreamDatasources{ id, name, projectName}, downstreamMetrics{ id, name, projectName},' \
               'downstreamLenses{ id, name}, downstreamVirtualConnections{ id, name, projectName} ' \
               'downstreamDashboards{ id, name}, downstreamSheets{ id, name, workbook{ id, name}, ' \
               'containedInDashboards{ id, name} }}, pageInfo {endCursor, hasNextPage }, totalCount} } '
COLUMN_QUERY = 'query PagedFieldsQuery($afterToken: String) {columnsConnection(first:1000, after: $afterToken){ nodes' \
               ' {id, vizportalId, luid, name, description, descriptionInherited{ assetId}, remoteType, isNullable, ' \
               'table { id, name, __typename, ... on DatabaseTable{ isCertified, database{ id, name, connectionType, ' \
               'isCertified, __typename }}}, downstreamFlows{ id, name, projectName}, downstreamWorkbooks{ id, name, ' \
               'projectName}, downstreamDatasources{ id, name, projectName}, downstreamMetrics{ id, name, projectName},' \
               'downstreamLenses{ id, name},' \
               'downstreamDashboards{ id, name}, downstreamSheets{ id, name, workbook{ id, name}, ' \
               'containedInDashboards{ id, name} }}, pageInfo {endCursor, hasNextPage }, totalCount} } '
FIELD_QUERY = "query PagedFieldsQuery($afterToken: String) {fieldsConnection(first:1000, after: $afterToken){ nodes {" \
              "id, name, fullyQualifiedName, description, descriptionInherited{ assetId, value}, isHidden, folderName, " \
              "__typename, datasource{ id, name, __typename}, sheets{ id, name, containedInDashboards{ id, name}. " \
              "workbook{ id, name}}, ... on BinField{ binSize, dataType, dataCategory, role, formula, fields{ id}}, " \
              "... on CalculatedField{ dataCategory, role, dataType, defaultFormat, semanticRole, aggregation, " \
              "aggregationParam, formula, isAutoGenerated, hasUserReference, fields{ id}}, " \
              "... on ColumnField{ dataType, dataCategory, role, defaultFormat, semanticRole, " \
              "aggregation, aggregationParam, columns{ id}}, ... on CombinedField{ fields{ id}}, " \
              "... on CombinedSetField{ delimiter, combinationType, fields{ id}},  ... on DatasourceField{ " \
              "remoteField{ id}}, ... on GroupField{ dataType, dataCategory, role, hasOther,fields{ id}}, " \
              "... on HierarchyField{ fields{ id}},... on SetField{ fields { id}}}, pageInfo{ endCursor, hasNextPage}, " \
              "totalCount}} "
DATASOURCE_QUERY = 'query PagedFieldsQuery($afterToken: String) {datasourcesConnection(first:1000, ' \
                   'after: $afterToken){ nodes { id, name, __typename, containsUnsupportedCustomSql, ' \
                   'hasUserReference, hasExtracts, extractLastRefreshTime, extractLastUpdateTime, createdAt, updatedAt,' \
                   'extractLastIncrementalUpdateTime, downstreamWorkbooks{ id, name}, ... on EmbeddedDatasource{ ' \
                   'workbook{ id, name}}, ... on PublishedDatasource{ luid, projectName, projectVizportalUrlId, ' \
                   'containerType, containerName, owner{ id, luid, name, email, domain, uri, username}, isCertified, ' \
                   'description, hasActiveWarning, uri, vizportalId, vizportalUrlId}}, pageInfo{ endCursor, ' \
                   'hasNextPage}, totalCount}} '
WORKBOOK_QUERY = "query PagedFieldsQuery($afterToken: String) {workbooksConnection(first:1000, after: $afterToken){ " \
                 "nodes {id, luid, name, __typename, containsUnsupportedCustomSql, description, createdAt, updatedAt, " \
                 "projectName, projectVizportalUrlId, containerType, containerName, owner{ id, luid, name, email, " \
                 "domain, uri, username}, uri, vizportalUrlId}, pageInfo{ endCursor, hasNextPage}, totalCount}}"
VIEW_QUERY = "query PagedFieldsQuery($afterToken: String) {viewsConnection(first:1000, after: $afterToken){ nodes {" \
             "id, luid, __typename, name, path, createdAt, updatedAt, index, workbook{ id, luid, owner{id, luid, email, username, name}}, " \
             "... on Sheet{ containedInDashboards{ id}, sheetFieldInstances{ id}}}, " \
             "pageInfo{ endCursor, hasNextPage}, totalCount}}"
METRIC_QUERY = 'query PagedFieldsQuery($afterToken: String) {metricsConnection(first:1000, after: $afterToken){ ' \
               'nodes{ id, luid, __typename, projectName, projectVizportalUrlId, vizportalUrlId, containerType, containerName, ' \
               'underlyingView{id}, description, name, owner{id, luid, name, email, domain, uri, username}, createdAt, ' \
               'updatedAt}, pageInfo{ endCursor, hasNextPage}, totalCount }}'
CONTENT_OWNER_QUERY = 'query PagedFieldsQuery($afterToken: String) {tableauUsersConnection(first:1000, ' \
                      'after: $afterToken) { nodes {id, luid, name, username, vizportalId, uri, domain, email, ' \
                      'contactForDatabases{ id, name, __typename, connectionType, isCertified}, contactForTables{ id, ' \
                      'name, __typename, isCertified}, ownedDatasources{ id, name, __typename, projectName, ' \
                      'isCertified}, ownedWorkbooks{ id, name, __typename, projectName}, ownedFlows{ id, name, ' \
                      '__typename, projectName}, ownedMetrics{ id, name, __typename, projectName}, ' \
                      'ownedVirtualConnections{ id, name, __typename, isCertified, projectName}, ' \
                      'authoredDataQualityWarnings{ id, warningType, __typename, message, asset{ id, name, ' \
                      '__typename}}, authoredDataQualityCertifications{ id, message, __typename, asset{ id, name, ' \
                      '__typename}}}, pageInfo{ endCursor, hasNextPage}, totalCount}}'
DATA_QUALITY_WARNING_QUERY = 'query PagedFieldsQuery($afterToken: String) {dataQualityWarningsConnection(first:1000, ' \
                             'after: $afterToken){ nodes{id, luid, author { id, name, email, username}, ' \
                             'authorDisplayName, vizportalId, isActive, isSevere, warningType, message, createdAt, ' \
                             'updatedAt, asset { id} }, pageInfo{ endCursor, hasNextPage}, totalCount }}'
DATA_QUALITY_CERTIFICATION_QUERY = 'query PagedFieldsQuery($afterToken: String) ' \
                                   '{dataQualityCertificationsConnection(first:1000, after: $afterToken){ nodes{ id, ' \
                                   'luid, author{ id, name, email, username}, authorDisplayName, vizportalId, isActive, ' \
                                   'message, createdAt, updatedAt, asset { id} }, pageInfo{ endCursor, hasNextPage}, ' \
                                   'totalCount }}'
FLOW_QUERY = 'query PagedFieldsQuery($afterToken: String) {flowsConnection(first:1000, after: $afterToken){ ' \
             'nodes{ id, luid, name, description, __typename, uri, vizportalUrlId, hasActiveWarning, projectName,' \
             'projectVizportalUrlId, personalSpaceUrlLink, containerType, containerName, containsUnsupportedCustomSql, ' \
             'owner { id, luid, name, email, domain, uri, username}, dataQualityWarning { id}, createdAt, updatedAt}, ' \
             'pageInfo{ endCursor, hasNextPage}, totalCount}}'
PARAMETER_QUERY = 'query PagedFieldsQuery($afterToken: String) {parametersConnection(first:1000, after: $afterToken)' \
                  '{nodes{ id, name, parentName, workbook{id}, datasource{id}, referencedByCalculations{id, __typename},' \
                  ' referencedByBins{id, __typename}, referencedBySets{id, __typename}}, pageInfo{ endCursor, ' \
                  'hasNextPage}, totalCount }}'
TAG_QUERY = 'query PagedFieldsQuery($afterToken: String) {tagsConnection(first:1000, after: $afterToken) {nodes{id, ' \
            'name, assets{id, __typename}}, pageInfo{ endCursor, hasNextPage}, totalCount }}'
LENS_QUERY = 'query PagedFieldsQuery($afterToken: String) {lensesConnection(first:1000, after: $afterToken) {nodes{id, ' \
             'name, luid, projectVizportalUrlId, vizportalUrlId, datasource{id, ... on PublishedDatasource{luid}, name}, ' \
             'owner{id, name, luid, email, username, domain, uri}, description, createdAt, updatedAt, __typename}, ' \
             'pageInfo{ endCursor, hasNextPage}, totalCount }}'
LENS_FIELD_QUERY = 'query PagedFieldsQuery($afterToken: String) {lensFieldsConnection(first:1000, after: $afterToken) ' \
                   '{nodes{id, name, description, datasourceField{id, name, __typename}, containingLens{ id, luid, ' \
                   'name}}, pageInfo{ endCursor, hasNextPage}, totalCount }}'
ASK_DATA_EXTENSION_QUERY = 'query PagedFieldsQuery($afterToken: String) {askDataExtensionsConnection(first:1000, ' \
                           'after: $afterToken) {nodes{id, lens{id, name, luid}, dashboard{ id, luid, name}}, ' \
                           'pageInfo{ endCursor, hasNextPage}, totalCount }}'
DATASOURCE_FILTER_QUERY = 'query PagedFieldsQuery($afterToken: String) {datasourceFiltersConnection(first:1000, ' \
                           'after: $afterToken) {nodes{id, field{id, name, __typename, ... on CalculatedField{ ' \
                          'hasUserReference, formula}}, datasource{ id, name, ... on PublishedDatasource{luid}}}, ' \
                           'pageInfo{ endCursor, hasNextPage}, totalCount }}'


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


def get_catalog_data(tableauserverclient, tableauserver, auth_token, abort_error):
    # Get the related objects' data from the Metadata API

    # Getting Sites
    print('{0}Attempting to get Sites ...{1}'.format(bcolors.OKBLUE, bcolors.ENDC))

    # Pass the query onto the metadata api
    site_list = get_query_results(tableauserver, 'tableauSites', SITES_QUERY, auth_token, abort_error)

    print('{0}Found {1} Site ...{2}'.format(bcolors.OKBLUE, len(site_list), bcolors.ENDC))

    # Getting the Databases
    print('{0}Attempting to get Databases ...{1}'.format(bcolors.OKBLUE, bcolors.ENDC))

    # Pass the query onto the metadata api
    try:
        database_list = get_paged_query_results(tableauserver, 'databasesConnection', DATABASE_QUERY,
                                                auth_token, abort_error)
    except IndexError as ie:
        print(ie)
        database_list = []

    print('{0}Found {1} Databases(s) ...{2}'.format(bcolors.OKBLUE, len(database_list), bcolors.ENDC))

    # Getting the Tables
    print('{0}Attempting to get Tables ...{1}'.format(bcolors.OKBLUE, bcolors.ENDC))

    # Pass the query onto the metadata api
    try:
        table_list = get_paged_query_results(tableauserver, 'tablesConnection', TABLE_QUERY, auth_token,
                                             abort_error)
    except IndexError as ie:
        print(ie)
        table_list = []

    print('{0}Found {1} Tables(s) ...{2}'.format(bcolors.OKBLUE, len(table_list), bcolors.ENDC))

    # Getting Table Columns
    print('{0}Attempting to get Columns ...{1}'.format(bcolors.OKBLUE, bcolors.ENDC))

    # Pass the query onto the metadata api
    try:
        column_list = get_paged_query_results(tableauserver, 'columnsConnection', COLUMN_QUERY, auth_token,
                                              abort_error)
    except IndexError as ie:
        print(ie)
        column_list = []

    print('{0}Found {1} Column(s) ...{2}'.format(bcolors.OKBLUE, len(column_list), bcolors.ENDC))

    # Getting Fields
    print('{0}Attempting to get Fields ...{1}'.format(bcolors.OKBLUE, bcolors.ENDC))

    # Pass the query onto the metadata api
    try:
        field_list = get_paged_query_results(tableauserver, 'fieldsConnection', FIELD_QUERY, auth_token,
                                             abort_error)
    except IndexError as ie:
        print(ie)
        field_list = []

    print('{0}Found {1} Field(s) ...{2}'.format(bcolors.OKBLUE, len(field_list), bcolors.ENDC))

    # Getting Virtual Connections
    print('{0}Attempting to get Virtual Connections ...{1}'.format(bcolors.OKBLUE, bcolors.ENDC))

    # Pass the query onto the metadata api
    try:
        virtual_connection_list = get_paged_query_results(tableauserver, 'virtualConnectionsConnection',
                                                          VCONN_QUERY, auth_token, abort_error)
    except IndexError as ie:
        print(ie)
        virtual_connection_list = []

    print('{0}Found {1} Virtual Connection(s) ...{2}'.format(bcolors.OKBLUE, len(virtual_connection_list),
                                                             bcolors.ENDC))

    # Getting Datasource
    print('{0}Attempting to get Datasources ...{1}'.format(bcolors.OKBLUE, bcolors.ENDC))

    # Pass the query onto the metadata api
    try:
        datasource_list = get_paged_query_results(tableauserver, 'datasourcesConnection', DATASOURCE_QUERY,
                                                  auth_token, abort_error)
    except IndexError as ie:
        print(ie)
        datasource_list = []

    print('{0}Found {1} Datasource(s) ...{2}'.format(bcolors.OKBLUE, len(datasource_list), bcolors.ENDC))

    # Getting Workbooks
    print('{0}Attempting to get Workbooks ...{1}'.format(bcolors.OKBLUE, bcolors.ENDC))

    # Pass the query onto the metadata api
    try:
        workbook_list = get_paged_query_results(tableauserver, 'workbooksConnection', WORKBOOK_QUERY,
                                                auth_token, abort_error)
    except IndexError as ie:
        print(ie)
        workbook_list = []

    print('{0}Found {1} Workbook(s) ...{2}'.format(bcolors.OKBLUE, len(workbook_list), bcolors.ENDC))

    # Getting Views
    print('{0}Attempting to get Dashboards and Sheets ...{1}'.format(bcolors.OKBLUE, bcolors.ENDC))

    # Pass the query onto the metadata api
    try:
        view_list = get_paged_query_results(tableauserver, 'viewsConnection', VIEW_QUERY, auth_token,
                                            abort_error)
    except IndexError as ie:
        print(ie)
        view_list = []

    print('{0}Found {1} Dashboard(s) and Sheet(s)...{2}'.format(bcolors.OKBLUE, len(view_list), bcolors.ENDC))

    # Getting Content Owners
    print('{0}Attempting to get Content Owners ...{1}'.format(bcolors.OKBLUE, bcolors.ENDC))

    # Pass the query onto the metadata api
    try:
        owner_liat = get_paged_query_results(tableauserver, 'tableauUsersConnection', CONTENT_OWNER_QUERY,
                                             auth_token, abort_error)
    except IndexError as ie:
        print(ie)
        owner_liat = []

    print('{0}Found {1} Content Owner(s) ...{2}'.format(bcolors.OKBLUE, len(owner_liat), bcolors.ENDC))

    # Print the status to the console
    print('{0}Attempting to get Metrics ...{1}'.format(bcolors.OKBLUE, bcolors.ENDC))

    # Pass the query onto the metadata api
    try:
        metric_list = get_paged_query_results(tableauserver, 'metricsConnection', METRIC_QUERY, auth_token,
                                              abort_error)
    except IndexError as ie:
        print(ie)
        metric_list = []

    print('{0}Found {1} Metrics(s) ...{2}'.format(bcolors.OKBLUE, len(metric_list), bcolors.ENDC))

    # Getting Data Quality Warnings
    print('{0}Attempting to get Data Quality Warnings ...{1}'.format(bcolors.OKBLUE, bcolors.ENDC))

    # Pass the query onto the metadata api
    try:
        dqw_list = get_paged_query_results(tableauserver, 'dataQualityWarningsConnection',
                                           DATA_QUALITY_WARNING_QUERY, auth_token, abort_error)
    except IndexError as ie:
        print(ie)
        dqw_list = []

    print('{0}Found {1} Data Quality Warning(s) ...{2}'.format(bcolors.OKBLUE, len(dqw_list), bcolors.ENDC))

    # Getting Data Quality Certifications
    print('{0}Attempting to get Data Quality Certifications ...{1}'.format(bcolors.OKBLUE, bcolors.ENDC))

    # Pass the query onto the metadata api
    try:
        dqc_list = get_paged_query_results(tableauserver, 'dataQualityCertificationsConnection',
                                           DATA_QUALITY_CERTIFICATION_QUERY, auth_token, abort_error)
    except IndexError as ie:
        print(ie)
        dqc_list = []

    print('{0}Found {1} Data Quality Certification(s) ...{2}'.format(bcolors.OKBLUE, len(dqc_list), bcolors.ENDC))

    # Getting Users
    print('{0}Attempting to get Users ...{1}'.format(bcolors.OKBLUE, bcolors.ENDC))

    # Pass the query onto the metadata api
    user_list = list(tableauserverclient.Pager(tableauserver.users))

    print('{0}Found {1} User(s) ...{2}'.format(bcolors.OKBLUE, len(user_list), bcolors.ENDC))

    # Getting Flows
    print('{0}Attempting to get Flows ...{1}'.format(bcolors.OKBLUE, bcolors.ENDC))

    # Pass the query onto the metadata api
    try:
        flow_list = get_paged_query_results(tableauserver, 'flowsConnection', FLOW_QUERY, auth_token,
                                            abort_error)
    except IndexError as ie:
        print(ie)
        flow_list = []

    print('{0}Found {1} Flow(s) ...{2}'.format(bcolors.OKBLUE, len(flow_list), bcolors.ENDC))

    # Getting Groups
    print('{0}Attempting to get Groups ...{1}'.format(bcolors.OKBLUE, bcolors.ENDC))

    # Pass the query onto the metadata api
    group_list = list(tableauserverclient.Pager(tableauserver.groups))

    print('{0}Found {1} Group(s) ...{2}'.format(bcolors.OKBLUE, len(group_list), bcolors.ENDC))

    # Getting Projects
    print('{0}Attempting to get Projects ...{1}'.format(bcolors.OKBLUE, bcolors.ENDC))

    # Pass the query onto the metadata api
    project_list = list(tableauserverclient.Pager(tableauserver.projects))

    print('{0}Found {1} Project(s) ...{2}'.format(bcolors.OKBLUE, len(project_list), bcolors.ENDC))

    # Print the status to the console
    print('{0}Attempting to get Parameters ...{1}'.format(bcolors.OKBLUE, bcolors.ENDC))

    # Pass the query onto the metadata api
    try:
        parameter_list = get_paged_query_results(tableauserver, 'parametersConnection', PARAMETER_QUERY,
                                                 auth_token, abort_error)
    except IndexError as ie:
        print(ie)
        parameter_list = []

    print('{0}Found {1} Parameter(s) ...{2}'.format(bcolors.OKBLUE, len(parameter_list), bcolors.ENDC))

    # Getting Tags
    print('{0}Attempting to get Tags ...{1}'.format(bcolors.OKBLUE, bcolors.ENDC))

    # Pass the query onto the metadata api
    try:
        tag_list = get_paged_query_results(tableauserver, 'tagsConnection', TAG_QUERY, auth_token,
                                           abort_error)
    except IndexError as ie:
        print(ie)
        tag_list = []

    print('{0}Found {1} Tag(s) ...{2}'.format(bcolors.OKBLUE, len(tag_list), bcolors.ENDC))

    # Getting Lenses
    print('{0}Attempting to get Lenses ...{1}'.format(bcolors.OKBLUE, bcolors.ENDC))

    # Pass the query onto the metadata api
    try:
        lenses_list = get_paged_query_results(tableauserver, 'lensesConnection', LENS_QUERY, auth_token,
                                              abort_error)
    except IndexError as ie:
        print(ie)
        lenses_list = []

    print('{0}Found {1} Lens(es) ...{2}'.format(bcolors.OKBLUE, len(lenses_list), bcolors.ENDC))

    # Getting Lens Fields
    print('{0}Attempting to get Lens Fields ...{1}'.format(bcolors.OKBLUE, bcolors.ENDC))

    # Pass the query onto the metadata api
    try:
        lens_fields_list = get_paged_query_results(tableauserver, 'lensFieldsConnection', LENS_FIELD_QUERY,
                                                   auth_token, abort_error)
    except IndexError as ie:
        print(ie)
        lens_fields_list = []

    print('{0}Found {1} Lens Field(s) ...{2}'.format(bcolors.OKBLUE, len(lens_fields_list), bcolors.ENDC))

    # Getting Ask Data Extensions
    print('{0}Attempting to get Ask Data Extensions ...{1}'.format(bcolors.OKBLUE, bcolors.ENDC))

    # Pass the query onto the metadata api
    try:
        ask_data_extensions_list = get_paged_query_results(tableauserver, 'askDataExtensionsConnection',
                                                           ASK_DATA_EXTENSION_QUERY, auth_token, abort_error)
    except IndexError as ie:
        print(ie)
        ask_data_extensions_list = []

    print('{0}Found {1} Ask Data Extension(s) ...{2}'.format(bcolors.OKBLUE, len(ask_data_extensions_list), bcolors.ENDC))

    # Getting Datasource Filters
    print('{0}Attempting to get Datasource Filter(s) ...{1}'.format(bcolors.OKBLUE, bcolors.ENDC))

    # Pass the query onto the metadata api
    try:
        datasource_filter_list = get_paged_query_results(tableauserver, 'datasourceFiltersConnection',
                                                           DATASOURCE_FILTER_QUERY, auth_token, abort_error)
    except IndexError as ie:
        print(ie)
        datasource_filter_list = []

    print(
        '{0}Found {1} Datasource Filter(s) ...{2}'.format(bcolors.OKBLUE, len(ask_data_extensions_list), bcolors.ENDC))

    catalog_data_dict = {'Sites': site_list, 'Databases': database_list, 'Tables': table_list, 'Columns': column_list,
                         'Fields': field_list, 'Virtual Connections': virtual_connection_list,
                         'Datasources': datasource_list, 'Workbooks': workbook_list, 'Views': view_list,
                         'Metrics': metric_list, 'Content Owners': owner_liat, 'Flows': flow_list,
                         'Data Quality Warnings': dqw_list, 'Data Quality Certifications': dqc_list,
                         'Groups': group_list, 'Users': user_list, 'Projects': project_list,
                         'Parameters': parameter_list, 'Tags': tag_list, 'Lenses': lenses_list,
                         'Lens Fields': lens_fields_list, 'Ask Data Extensions': ask_data_extensions_list,
                         'Datasource Filters': datasource_filter_list}

    return catalog_data_dict


def get_query_results(tableauserver, table_type, query, auth_token, abort_error_value):
    # sign out of current session
    # tableauserver.auth.sign_out()
    # print("Signing out")
    # # sign back in
    # tableauserver.auth.sign_in(auth_token)
    # print("Signing in")

    df_results = []

    query_results = tableauserver.metadata.query(query, abort_on_error=abort_error_value)
    tableau_assets = query_results['data'][table_type]
    for row in tableau_assets:
        df_results.append(row)

    return df_results


def get_paged_query_results(tableauserver, table_type, query, auth_token, abort_error_value):
    # sign out of current session
    # tableauserver.auth.sign_out()
    # print("Signing out")
    # # sign back in
    # tableauserver.auth.sign_in(auth_token)
    # print("Signing in")

    df_results = []
    try:
        paged_query_results = tableauserver.metadata.paginated_query(query, variables={'first': 1000, 'afterToken': None}, abort_on_error=abort_error_value)
        for results_page in paged_query_results['pages']:
            nodes = results_page['data'][table_type]['nodes']
            for row in nodes:
                df_results.append(row)
    except Exception as e:
        print(e)

    return df_results
