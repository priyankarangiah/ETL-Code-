import requests
import json
import time
import pandas
from datetime import datetime


def get_data(request_url):
    print('requesting from:')
    print(request_url)
    response = requests.get(request_url)
    print(response.status_code)
    print(response.json())
    return response.json()


if __name__ == "__main__":
    urls = ['http://10.43.212.75/api/v1/print_job','http://10.43.212.75/api/v1/printer','http://10.43.212.75/api/v1/history/print_jobs']
    REST_API_URL = 'https://api.powerbi.com/beta/bc876b21-f134-4c12-a265-8ed26b7f0f3b/datasets/5a38ab0f-5cc0-406d-a0ae-a857d69290d8/rows?key=s2YRCfT9yYbssNZ%2BW1w%2FWAdIRZe8MpRTx5bA83%2BKpjilUul8rLP8DRCa%2FS8IMy9mdeEEl4UcsR23A2T%2BjzJUfw%3D%3D'

    start_time = time.time()
    end_time = time.time()

    data_paraBI = {}

    # loop to get data from the machine
    while end_time-start_time < 43300:
        data_raw = []
        for i in range(1):
            json_data = get_data(urls[0])
            url0_data = [
                json_data.get('datetime_cleaned','not here'),
                json_data.get('datetime_finished','not here'),
                json_data.get('datetime_started','not here'),
                json_data.get('name','not here'),
                json_data.get('progress','not here'),
                # json_data.get('reprint_original_uuid','not here'),
                json_data.get('result', 'not here'),
                json_data.get('source','not here'),
                # json_data.get('source_appliction','not here'),
                json_data.get('source_user','not here'),
                json_data.get('state','not here'),
                json_data.get('time_elapsed', 'not here'),
                json_data.get('time_total','not here'),
                # json_data.get('uuid','not here')
            ]
            #add code
            data_paraBI['datetime_cleaned'] = json_data.get('datetime_cleaned')
            data_paraBI['datetime_finished'] = json_data.get('datetime_finished')
            data_paraBI['datetime_started'] = json_data.get('datetime_started')
            data_paraBI['name'] = json_data.get('name')
            data_paraBI['progress'] = json_data.get('progress')
            # data_paraBI['reprint_original_uuid'] = json_data.get('reprint_original_uuid')
            data_paraBI['result'] = json_data.get('result')
            data_paraBI['source'] = json_data.get('source')
            # data_paraBI['source_application'] = json_data.get('source_appliction')
            data_paraBI['source_user'] = json_data.get('source_user')
            data_paraBI['state'] = json_data.get('state')
            data_paraBI['time_elapsed'] = json_data.get('time_elapsed')
            data_paraBI['time_total'] =  json_data.get('time_total')
            # data_paraBI['uuid'] = json_data.get('uuid')

            data_raw.append(url0_data)
            print('Raw data -', data_raw)

            json_data = get_data(urls[1])
            url1_data = [
                json_data['bed']['pre_heat']['active'],
                json_data['bed']['temperature']['current'],
                json_data['bed']['temperature']['target'],
                # json_data['heads'][0]['extruders'][0]['active_material']['GUID'],
                # json_data['heads'][0]['extruders'][0]['active_material']['guid'],
                json_data['heads'][0]['extruders'][0]['feeder']['acceleration'],
                json_data['heads'][0]['extruders'][0]['feeder']['jerk'],
                json_data['heads'][0]['extruders'][0]['feeder']['max_speed'],
                # json_data['heads'][0]['extruders'][0]['hotend']['id'],
                json_data['heads'][0]['extruders'][0]['hotend']['offset']['state'],
                json_data['heads'][0]['extruders'][0]['hotend']['offset']['x'],
                json_data['heads'][0]['extruders'][0]['hotend']['offset']['y'],
                json_data['heads'][0]['extruders'][0]['hotend']['offset']['z'],
                # json_data['heads'][0]['extruders'][0]['hotend']['serial'],
                # json_data['heads'][0]['extruders'][0]['hotend']['statistics']['last_material_guid'],
                json_data['heads'][0]['extruders'][0]['hotend']['statistics']['material_extruded'],
                json_data['heads'][0]['extruders'][0]['hotend']['statistics']['max_temperature_exposed'],
                json_data['heads'][0]['extruders'][0]['hotend']['statistics']['time_spent_hot'],
                json_data['heads'][0]['extruders'][0]['hotend']['temperature']['current'],
                json_data['heads'][0]['extruders'][0]['hotend']['temperature']['target'],
                # json_data['heads'][0]['extruders'][1]['active_material']['GUID'],
                # json_data['heads'][0]['extruders'][1]['active_material']['guid'],
                json_data['heads'][0]['extruders'][1]['active_material']['length_remaining'],
                json_data['heads'][0]['extruders'][1]['feeder']['acceleration'],
                json_data['heads'][0]['extruders'][1]['feeder']['jerk'],
                json_data['heads'][0]['extruders'][1]['feeder']['max_speed'],
                # json_data['heads'][0]['extruders'][1]['hotend']['id'],
                # json_data['heads'][0]['extruders'][1]['hotend']['offset']['state'],
                json_data['heads'][0]['extruders'][1]['hotend']['offset']['x'],
                json_data['heads'][0]['extruders'][1]['hotend']['offset']['y'],
                json_data['heads'][0]['extruders'][1]['hotend']['offset']['z'],
                json_data['heads'][0]['extruders'][1]['hotend']['serial'],
                # json_data['heads'][0]['extruders'][1]['hotend']['statistics']['last_material_guid'],
                # json_data['heads'][0]['extruders'][1]['hotend']['statistics']['material_extruded'],
                json_data['heads'][0]['extruders'][1]['hotend']['statistics']['max_temperature_exposed'],
                json_data['heads'][0]['extruders'][1]['hotend']['statistics']['time_spent_hot'],
                json_data['heads'][0]['extruders'][1]['hotend']['temperature']['current'],
                json_data['heads'][0]['extruders'][1]['hotend']['temperature']['target'],
                json_data['heads'][0]['fan'],
                json_data['heads'][0]['jerk']['x'],
                json_data['heads'][0]['jerk']['y'],
                json_data['heads'][0]['jerk']['z'],
                json_data['heads'][0]['max_speed']['x'],
                json_data['heads'][0]['max_speed']['y'],
                json_data['heads'][0]['max_speed']['z'],
                json_data['heads'][0]['position']['x'],
                json_data['heads'][0]['position']['y'],
                json_data['heads'][0]['position']['z'],
                json_data['led']['brightness'],
                json_data['led']['hue'],
                json_data['led']['saturation'],
                json_data['network']['ethernet']['connected'],
                json_data['network']['ethernet']['enabled'],
                json_data['network']['wifi']['connected'],
                json_data['network']['wifi']['enabled'],
                json_data['network']['wifi']['mode'],
                json_data['network']['wifi']['ssid'],
                json_data['status']
            ]
            #add code
            data_paraBI['bed-pre_heat-active'] = json_data['bed']['pre_heat']['active']
            data_paraBI['bed-temperature-current'] = json_data['bed']['temperature']['current']
            data_paraBI['bed-temperature-target'] = json_data['bed']['temperature']['target']
            # data_paraBI['extruder-1-active-material-GUID'] = json_data['heads'][0]['extruders'][0]['active_material']['GUID']
            # data_paraBI['extruder-1-active-material-guid'] = json_data['heads'][0]['extruders'][0]['active_material']['guid']
            data_paraBI['extruder-1-feeder-acceleration'] = json_data['heads'][0]['extruders'][0]['feeder']['acceleration']
            data_paraBI['extruder-1-feeder-jerk'] = json_data['heads'][0]['extruders'][0]['feeder']['jerk']
            data_paraBI['extruder-1-feeder-max_speed'] = json_data['heads'][0]['extruders'][0]['feeder']['max_speed']
            # data_paraBI['extruder-1-hotend-id'] = json_data['heads'][0]['extruders'][0]['hotend']['id']
            data_paraBI['extruder-1-hotend-offset-state'] = json_data['heads'][0]['extruders'][0]['hotend']['offset']['state']
            data_paraBI['extruder-1-hotend-offset-x'] = json_data['heads'][0]['extruders'][0]['hotend']['offset']['x']
            data_paraBI['extruder-1-hotend-offset-y'] = json_data['heads'][0]['extruders'][0]['hotend']['offset']['y']
            data_paraBI['extruder-1-hotend-offset-z'] = json_data['heads'][0]['extruders'][0]['hotend']['offset']['z']
            # data_paraBI['extruder-1-hotend-serial'] = json_data['heads'][0]['extruders'][0]['hotend']['serial']
            # data_paraBI['extruder-1-hotend-statistics-last_material_guid'] = json_data['heads'][0]['extruders'][0]['hotend']['statistics']['last_material_guid']
            data_paraBI['extruder-1-hotend-statisics-material_extruded'] = json_data['heads'][0]['extruders'][0]['hotend']['statistics']['material_extruded']
            data_paraBI['extruder-1-hotend-statistics-max_temperature_exposed'] = json_data['heads'][0]['extruders'][0]['hotend']['statistics']['max_temperature_exposed']
            data_paraBI['extruder-1-hotend-statistics-time_spent_hot'] = json_data['heads'][0]['extruders'][0]['hotend']['statistics']['time_spent_hot']
            data_paraBI['extruder-1-hotend-current-temperature'] = json_data['heads'][0]['extruders'][0]['hotend']['temperature']['current']
            data_paraBI['extruder-1-hotend-target-temperature'] = json_data['heads'][0]['extruders'][0]['hotend']['temperature']['target']
            # data_paraBI['extruder-2-hotend-active_material_GUID'] = json_data['heads'][0]['extruders'][1]['active_material']['GUID']
            # data_paraBI['extruder-2-hotend-active_material_guid'] = json_data['heads'][0]['extruders'][1]['active_material']['guid']
            data_paraBI['extruder-2-hotend-active_material-length_remaining'] = json_data['heads'][0]['extruders'][1]['active_material']['length_remaining']
            data_paraBI['extruder-2-hotend-feeder-acceleration'] = json_data['heads'][0]['extruders'][1]['feeder']['acceleration']
            data_paraBI['extruder-2-hotend-feeder-jerk'] = json_data['heads'][0]['extruders'][1]['feeder']['jerk']
            data_paraBI['extruder-2-hotend-feeder-max_speed'] = json_data['heads'][0]['extruders'][1]['feeder']['max_speed']
            # data_paraBI['extruder-2-hotend-id'] = json_data['heads'][0]['extruders'][1]['hotend']['id']
            # data_paraBI['extruder-2-hotend-offset-state'] = json_data['heads'][0]['extruders'][1]['hotend']['offset']['state']
            data_paraBI['extruder-2-hotend-offset-x'] = json_data['heads'][0]['extruders'][1]['hotend']['offset']['x']
            data_paraBI['extruder-2-hotend-offset-y'] = json_data['heads'][0]['extruders'][1]['hotend']['offset']['y']
            data_paraBI['extruder-2-hotend-offset-z'] = json_data['heads'][0]['extruders'][1]['hotend']['offset']['z']
            # data_paraBI['extruder-2-hotend-serial'] = json_data['heads'][0]['extruders'][1]['hotend']['serial']
            # data_paraBI['extruder-2-hotend-statistics-last_material_guid'] = json_data['heads'][0]['extruders'][1]['hotend']['statistics']['last_material_guid']
            data_paraBI['extruder-2-hotend-statistics-material_extruded'] = json_data['heads'][0]['extruders'][1]['hotend']['statistics']['material_extruded']
            data_paraBI['extruder-2-hotend-statistics-max_temperature_exposed'] = json_data['heads'][0]['extruders'][1]['hotend']['statistics']['max_temperature_exposed']
            data_paraBI['extruder-2-hotend-statistics-time_spent_hot'] = json_data['heads'][0]['extruders'][1]['hotend']['statistics']['time_spent_hot']
            data_paraBI['extruder-2-hotend-current-temperature'] = json_data['heads'][0]['extruders'][1]['hotend']['temperature']['current']
            data_paraBI['extruder-2-hotend-target-temperature'] = json_data['heads'][0]['extruders'][1]['hotend']['temperature']['target']
            data_paraBI['heads-fan'] = json_data['heads'][0]['fan']
            data_paraBI['heads-jerk-x'] = json_data['heads'][0]['jerk']['x']
            data_paraBI['heads-jerk-y'] = json_data['heads'][0]['jerk']['y']
            data_paraBI['heads-jerk-z'] = json_data['heads'][0]['jerk']['z']
            data_paraBI['heads-max_speed-x'] = json_data['heads'][0]['max_speed']['x']
            data_paraBI['heads-max_speed-y'] = json_data['heads'][0]['max_speed']['y']
            data_paraBI['heads-max_speed-z'] = json_data['heads'][0]['max_speed']['z']
            data_paraBI['heads-position-x'] = json_data['heads'][0]['position']['x']
            data_paraBI['heads-position-y'] = json_data['heads'][0]['position']['y']
            data_paraBI['heads-position-z'] = json_data['heads'][0]['position']['z']
            data_paraBI['led-brightness'] = json_data['led']['brightness']
            data_paraBI['led-hue'] = json_data['led']['hue']
            data_paraBI['led-saturation'] = json_data['led']['saturation']
            data_paraBI['network-ethernet-connected'] = json_data['network']['ethernet']['connected']
            data_paraBI['network-ethernet-enabled'] = json_data['network']['ethernet']['enabled']
            data_paraBI['network-wifi-connected'] = json_data['network']['wifi']['connected']
            data_paraBI['network-wifi-enabled'] = json_data['network']['wifi']['enabled']
            data_paraBI['network-wifi-mode'] = json_data['network']['wifi']['mode']
            data_paraBI['network-wifi-ssid'] = json_data['network']['wifi']['ssid']
            data_paraBI['status'] = json_data['status']
        
            
            data_raw.append(url1_data)
            print('Raw data -', data_raw)
            

            # json_data = get_data(urls[2])
            # url2_data = [
            #      json_data[0]['datetime_cleaned'],
            #      json_data[0]['datetime_finished'],
            #      json_data[0]['datetime_started'],
            #      json_data[0]['name'],
            #      json_data[0]['reprint_original_uuid'],
            #      json_data[0]['result'],
            #      json_data[0]['source'],
            #      json_data[0]['time_elapsed'],
            #      json_data[0]['time_estimated'],
            #      json_data[0]['time_total'],
            #      json_data[0]['uuid']
            #  ]

            # #add code
            # data_paraBI['datetime_cleaned'] = json_data[0]['datetime_cleaned']
            # data_paraBI['datetime_finished'] = json_data[0]['datetime_finished']
            # data_paraBI['datetime_started'] =  json_data[0]['datetime_started']
            # data_paraBI['name'] = json_data[0]['name']
            # data_paraBI['reprint_original_uuid'] = json_data[0]['reprint_original_uuid']
            # data_paraBI['result'] =  json_data[0]['result']
            # data_paraBI['source'] = json_data[0]['source']
            # data_paraBI['time_elapsed'] = json_data[0]['time_elapsed']
            # data_paraBI['time_estimated'] = json_data[0]['time_estimated']
            # data_paraBI['time_total'] = json_data[0]['time_total']
            # data_paraBI['uuid'] =  json_data[0]['uuid']
            

            # data_raw.append(url2_data)
            # print('Raw data -', data_raw)

        datetime_cleaned = url0_data[0]
        #print("debuging",datetime_cleaned)
        datetime_object = datetime.strptime(datetime_cleaned, "%Y-%m-%dT%H:%M:%S") if datetime_cleaned else None
        url0_data[0] = datetime_object
        datetime_finished = url0_data[1]
        datetime_object = datetime.strptime(datetime_finished, "%Y-%m-%dT%H:%M:%S") if datetime_finished else None
        url0_data[1] = datetime_object
        datetime_started = url0_data[2]
        datetime_object = datetime.strptime(datetime_started, "%Y-%m-%dT%H:%M:%S") if datetime_started else None
        url0_data[2] = datetime_object
        # datetime_cleaned  = url2_data[0]
        # datetime_object = datetime.strptime(datetime_cleaned, "%Y-%m-%dT%H:%M:%S") if datetime_cleaned else None
        # url2_data[0] = datetime_object
        # datetime_finished = url2_data[1]
        # datetime_object = datetime.strptime(datetime_finished, "%Y-%m-%dT%H:%M:%S") if datetime_finished else None
        # url2_data[1] = datetime_object
        # datetime_started = url2_data[2]
        # datetime_object = datetime.strptime(datetime_started, "%Y-%m-%dT%H:%M:%S") if datetime_started else None
        # url2_data[2] = datetime_object


        # this line will tell you the data type of the datetime object (string)
        print(type(url0_data[0]))

        end_time = time.time()

        # combining data from multiple lists into one list
        all_data = url0_data.extend(url1_data)

        # add all headers
        HEADER = ['datetime_cleaned','datetime_finished','datetime_started','name','progress','reprint_original_uuid','result','source','source_application','source_user','state','time_elapsed','time_total','uuid','bed_pre_heat_active','current_bed_temp','target_bed_temp','extruder_1_active_material_GUID','extruder_1_active_material_guid','extruder_1_acceleration','extruder_1_jerk','extruder_1_maxspeed','extruder_1_id','extruder_1_offset_state','extruder_1_offset_x','extruder_1_offset_y','extruder_1_offset_z','extruder_1_serial','extruder_1_last_material_guid','extruder_1_material_extruded','extruder_1_temperature_exposed','extruder_1_time_spent_hot','extruder_1_current_temperature','extruder_1_target_temperature','extruder_2_active_material_GUID','extruder_2_active_material_guid','extruder_2_active_material_length_remaining','extruder_2_acceleration','extruder_2_feeder_jerk','extruder_2_max_speed','extruder_2_id','extruder_2_offset_state','extruder_2_offset_x','extruder_2_offset_y','extruder_2_offset_z','extruder_2_serial','extruder_2_last_material_guid','extruder_2_material_extruded','extruder_2_max_temperature_exposed','extruder_2_time_spent_hot','extruder_2_current_temperature','extruder_2_target_temperature','head_fan','head_jerk_x','head_jerk_y','head_jerk_z','head_maxspeed_x','head_maxspeed_y','head_maxspeed_z','head_position_x','head_position_y','head_position_z','led_breightness','led_hue','led_saturation','network_ethernt_connected','network_ethernet_enabled','network_wifi_connected','network_wifi_enabled','network_wifi_mode','network_wifi_ssid','print_status']
        print("starting ****************************************")
        print(all_data,type(all_data))
        print(data_paraBI,type(data_paraBI))
        
        print("ending *****************************************************8")

        
        data_df = pandas.DataFrame(all_data, data_paraBI)
        json_data = bytes(data_df.to_json(orient='records'), encoding='utf-8')
        print('JSON dataset', json_data)

        # a = {}
        # k = 0
        # while k < 10:
        #     json_data = get_data(urls[0])
        #     url0_data = [
        #         json_data.get('datetime_cleaned','not here'),
        #         json_data.get('datetime_finished','not here'),
        #         json_data.get('datetime_started','not here'),
        #         json_data.get('name','not here'),
        #         json_data.get('progress','not here'),
        #         json_data.get('reprint_original_uuid','not here'),
        #         json_data.get('result', 'not here'),
        #         json_data.get('source','not here'),
        #         json_data.get('source_appliction','not here'),
        #         json_data.get('source_user','not here'),
        #         json_data.get('state','not here'),
        #         json_data.get('time_elapsed', 'not here'),
        #         json_data.get('time_total','not here'),
        #         json_data.get('uuid','not here')
        #     ]
        #     values = ('datetime_cleaned','datetime_finished','datetime_started','name','progress','reprint_original_uuid','result','source','source_application','source_user','state','time_elapsed','time_total','uuid')
        #     a[url0_data] = values
        #     k += 1
        #     data_raw.append(url0_data)
        #     print('Raw data -', data_raw)



        # data = {}
        # # for i in range(1): 
        #     data[json_data.get('datetime_cleaned','not here')]= 'datetime_cleaned'
        #     # json_data = json.dumps(data)
        #     print(datetime_cleaned)

        # Post the data on the Power BI API

        json_data_paraBI = json.dumps(data_paraBI)
        print("DEBUG ?????")
        print(json_data_paraBI)
        req = requests.post(REST_API_URL, json_data_paraBI)

        print('Data posted in Power BI API')
    