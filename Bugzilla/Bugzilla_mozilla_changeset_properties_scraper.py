           'SERVER=QUOCBUI\MSSQLSERVER01;' \
        VALUES (source.Changeset_Hash_ID, source.Previous_File_Name, source.Updated_File_Name, ?, SYSUTCDATETIME())
    max_retries = 20
        while attempt_number <= max_retries:
            if response.status_code == 200:  # OK
            # elif response.status_code == 429:  # Code 429: Reach max request limit rate
            else:
                print(f"{str(response.status_code)}.")
                print(f"Wake up.\nRetrying...", end="", flush=True)
            if attempt_number == max_retries:
                print(f"Too many failed request attempts. Request url: {request_url}. Exit program.")
            diff_git_line = lines[0]    # Ignore line[0]
    max_retries = 20
        while attempt_number <= max_retries:
            # elif response.status_code == 429:   # Code 429: Reach max request limit rate
            else:
                print(f"{str(response.status_code)}.")
                print(f"Wake up.\nRetrying...", end="", flush=True)
            if attempt_number == max_retries:
                print(f"Too many failed request attempts. Request url: {request_url}. Exit program.")
            save_changeset_properties_query_batches = []
            batch_count = 0
            batch_size_limit = 100

            # Build batches of queries
                    batch_count += 1
                    if batch_count == batch_size_limit:
                        save_changeset_properties_query_batches.append((save_changeset_properties_queries, params))
                        save_changeset_properties_queries = ''
                        params = []
                        batch_count = 0

            # Add any remaining queries to the last batch
            if save_changeset_properties_queries:
                save_changeset_properties_query_batches.append((save_changeset_properties_queries, params))

            # Execute batches of queries
            for batch_query, batch_params in save_changeset_properties_query_batches:
                cursor.execute(batch_query, batch_params)
             # Commit the transaction
            conn.commit() 
    # list_of_records = get_records_to_process(1, 34124, 45454) # Test
    # list_of_records.append(('4400', '0f16abb82c08d5033af4caea5f21a48fb5c267b2', '840877', '/mozilla-central/rev/0f16abb82c08d5033af4caea5f21a48fb5c267b2', None)) # Test case for deleted, new, renamed, copied file names