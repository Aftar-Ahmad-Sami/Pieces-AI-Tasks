# # import pieces_os_client
# # import platform
# # import json

# # # Defining the port based on the operating system. For Linux, the port is 5323, and for macOS/Windows, the port is 1000.
# # platform_info = platform.platform()
# # if 'Linux' in platform_info:
# #     port = 5323
# # else:
# #     port = 1000

# # # The `basePath` defaults to http://localhost:1000, however we need to change it to the correct port based on the operating system.
# # configuration = pieces_os_client.Configuration(host=f"http://localhost:{port}")

# # # Initialize the Pieces ApiClient
# # api_client = pieces_os_client.ApiClient(configuration)

# # # Enter a context with an instance of the ApiClient
# # with pieces_os_client.ApiClient(configuration) as api_client:
# #     # Create an instance of the WellKnownApi class
# #     api_instance = pieces_os_client.WellKnownApi(api_client)

# #     try:
# #         # Retrieve the (wellknown) health of the Pieces OS
# #         # api_response = api_instance.get_well_known_health()
# #         api_response = api_instance.get_well_known_health()
# #         print("The response of WellKnownApi().get_well_known_health:")
# #         print(api_response) # Response: ok
# #     except Exception as e:
# #         print("Exception when calling WellKnownApi->get_well_known_health: %s\n" % e)

# import pieces_os_client
# from pieces_os_client import WellKnownApi, ModelsApi, QGPTStreamOutput, QGPTStreamInput
# from websocket import WebSocketConnectionClosedException
# import platform

# platform_info = platform.platform()
# port = 5323 if 'Linux' in platform_info else 1000
# configuration = pieces_os_client.Configuration(host=f"http://localhost:{port}")
# api_client = pieces_os_client.ApiClient(configuration)
# version = WellKnownApi(api_client).get_well_known_version()
# health = WellKnownApi(api_client).get_well_known_health()

# models = ModelsApi(api_client).models_snapshot()
# for model in models.iterable:
#     print(model.name, model.id) 

# for model in models.iterable:
#     if model.cloud or model.downloaded:
#         print(model.name, model.id)

# class AskStreamWS:
#     ws = AskStreamWS()
#     ws.send_message(
#         QGPTStreamInput(
#             question=QGPTQuestionInput(
#                 query="Hello",
#                 application = application.id,
#                 model=model.id
#             ),
#             conversation=conversation_id
#         )
#     )