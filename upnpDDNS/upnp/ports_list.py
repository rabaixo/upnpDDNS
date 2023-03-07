# default port list
ports_list = [
                {
                    "ExternalPort": 9898,
                    "Protocol": 'TCP',
                    "InternalPort": 80,
                    "Description":'HTTP server'
                },
                {
                    "ExternalPort": 1194,
                    "Protocol": 'UDP',
                    "InternalPort": 1194,
                    "Description": 'Vpn server'
                },
                {
                    "ExternalPort": 8989,
                    "Protocol": 'UDP',
                    "InternalPort": 22,
                    "Description": 'Vpn server'
                },

            ]