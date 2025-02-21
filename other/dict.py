dict1 = { "batters":
          { "batter":
            [{ "batter":
                [{ "batter":
                    [{ 
                        "type": "Regular"
                    }] 
                }] 
             }] 
          }
        } 

typing = dict1['batters']['batter'][0]['batter'][0]['batter'][0]['type']
print(typing)