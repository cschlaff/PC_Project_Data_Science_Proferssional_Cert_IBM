spacex_df.loc[(spacex_df['Payload Mass (kg)']>=value.min()) & (spacex_df['Payload Mass (kg)']<= value.max()) & (dataFrame['JOB'].str.startswith('D')),
                    ['Name','JOB']])


