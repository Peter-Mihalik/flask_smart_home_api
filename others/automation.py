from flask.globals import request
import requests
import urllib

# Create new devices and save them

# devices = {
#     'livingroom': {
#         'light': requests.get(
#             'http://home_automation.iamroot.eu/newSmartLight').json()['id'],
#         'switch': requests.get(
#             'http://home_automation.iamroot.eu/newSwitchSensor').json()['id'],
#         'motion-sensor': requests.get(
#             'http://home_automation.iamroot.eu/newMotionSensor').json()['id'],
#         'smart-plug': requests.get(
#             'http://home_automation.iamroot.eu/newSmartPlug').json()['id']
#     },
#     'kitchen': {
#         'light': requests.get(
#             'http://home_automation.iamroot.eu/newSmartLight').json()['id'],
#         'switch': requests.get(
#             'http://home_automation.iamroot.eu/newSwitchSensor').json()['id'],
#         'motion-sensor': requests.get(
#             'http://home_automation.iamroot.eu/newMotionSensor').json()['id'],
#         'smart-plug': requests.get(
#             'http://home_automation.iamroot.eu/newSmartPlug').json()['id']
#     },
#     'bathroom': {
#         'light': requests.get(
#             'http://home_automation.iamroot.eu/newSmartLight').json()['id'],
#         'switch': requests.get(
#             'http://home_automation.iamroot.eu/newSwitchSensor').json()['id'],
#         'smart-plug': requests.get(
#             'http://home_automation.iamroot.eu/newSmartPlug').json()['id']
#     },
#     'karsobs room': {
#         'light': requests.get(
#             'http://home_automation.iamroot.eu/newSmartLight').json()['id'],
#         'switch': requests.get(
#             'http://home_automation.iamroot.eu/newSwitchSensor').json()['id'],
#         'smart-plug': requests.get(
#             'http://home_automation.iamroot.eu/newSmartPlug').json()['id']
#     },
#     'karliks room': {
#         'light': requests.get(
#             'http://home_automation.iamroot.eu/newSmartLight').json()['id'],
#         'switch': requests.get(
#             'http://home_automation.iamroot.eu/newSwitchSensor').json()['id'],
#         'smart-plug': requests.get(
#             'http://home_automation.iamroot.eu/newSmartPlug').json()['id']
#     },
#     'julias room': {
#         'light': requests.get(
#             'http://home_automation.iamroot.eu/newSmartLight').json()['id'],
#         'switch': requests.get(
#             'http://home_automation.iamroot.eu/newSwitchSensor').json()['id'],
#         'smart-plug': requests.get(
#             'http://home_automation.iamroot.eu/newSmartPlug').json()['id']
#     },
#     'karloss room': {
#         'light': requests.get(
#             'http://home_automation.iamroot.eu/newSmartLight').json()['id'],
#         'switch': requests.get(
#             'http://home_automation.iamroot.eu/newSwitchSensor').json()['id'],
#         'smart-plug': requests.get(
#             'http://home_automation.iamroot.eu/newSmartPlug').json()['id']
#     }
# }

# print(devices)

devices = {
    'livingroom': {
        'light': '9b18303c-5630-4256-ba63-88bc530a38e1',
        'switch': '36260ff6-c936-4bc3-a6d0-8445b606af12',
        'motion-sensor': '16791e0b-69c2-4e62-919f-f1eb0296ca6a',
        'smart-plug': '8615d7a5-ac68-49a6-bf29-40e693fa28e7'},
    'kitchen': {
        'light': '993b94a8-a92d-4758-8a32-787ae008d3a6',
        'switch': '287beef9-da2d-4a7f-9518-de2185915a90',
        'motion-sensor': '070e5685-65fc-48b6-8fc4-d3e8c19ed36d',
        'smart-plug': 'ffdf6351-4589-40d3-b822-b301772f5421'},
    'bathroom': {
        'light': 'ff042c4b-28d9-4ebe-aa37-b3de61ac80cc',
        'switch': '5f8be8b8-5594-4f36-be43-6c130cca8396',
        'smart-plug': 'c1df3780-d7da-4df6-936a-f4f809d1f0d9'},
    'karsobs room': {
        'light': '95c81245-37f5-455b-b045-3b4665cf5176',
        'switch': 'a3cebc1c-ead8-4e36-9c04-1d54e29de872',
        'smart-plug': '3b388755-8dbf-4919-aba3-884ad1888fc4'},
    'karliks room': {
        'light': '4515542a-68de-4a33-b20d-39d34e2582be',
        'switch': '403af07c-e5c2-43a8-9243-d60bfe2e966f',
        'smart-plug': '06a521df-3394-4b00-b78c-19c9ffa84585'},
    'julias room': {
        'light': 'c5c82596-a1c1-494b-b713-ccf4d5782d10',
        'switch': '92921bd8-e37f-4cd0-a7c0-db5c5b708a20',
        'smart-plug': '800378e2-875d-40a8-983d-af8029e8a28b'},
    'karloss room': {
        'light': '1b9ac043-bb23-4620-83da-8a681be3ca19',
        'switch': 'de5ecd73-9e95-40e6-9b92-5a7e62587f35',
        'smart-plug': '9a84b84a-1838-4346-adc5-cfe45da9fbaf'}
}
# Change Motion Sensor Response Adreses
# l_room_m_sensor_id = devices['livingroom']['motion-sensor']
# l_room_light_id = devices['livingroom']['light']
# l_room_light_url = 'http://home_automation.iamroot.eu/device/' + \
#     l_room_light_id+'/state/on'

# kitchen_m_sensor_id = devices['kitchen']['motion-sensor']
# kitchen_light_id = devices['kitchen']['light']
# kitchen_light_url = 'http://home_automation.iamroot.eu/device/' + \
#     kitchen_light_id+'/state/on'

# requests.get('http://home_automation.iamroot.eu/device/'+l_room_m_sensor_id +
#              '/report_url?url=' + urllib.parse.quote_plus(l_room_light_url))
# requests.get('http://home_automation.iamroot.eu/device/'+kitchen_m_sensor_id +
#              '/report_url?url=' + urllib.parse.quote_plus(kitchen_light_url))
# print('http://home_automation.iamroot.eu/device/'+l_room_m_sensor_id,
#       'http://home_automation.iamroot.eu/device/' + kitchen_m_sensor_id)

# Change report Url on switches
# for key, value in devices.items():
#     requests.get('http://home_automation.iamroot.eu/device/' +
#                  value['switch']+'/report_url?url='+urllib.parse.quote_plus('http://home_automation.iamroot.eu/device/'+value['light']+'/toggle'))
#     print('http://home_automation.iamroot.eu/device/'+value['switch'])

# Chenge light tepmreature to default 3500
for key, value in devices.items():
    ip = value['light']
    url = 'http://home_automation.iamroot.eu/device/'+ip+'/color_temperature/3500'
    req = requests.get(url).json()['color_temperature']
    print(req)
