# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore


# project_id = 'farmaciasapi'
# cred = credentials.ApplicationDefault()
# firebase_admin.initialize_app(cred, {
#   'projectId': project_id,
# })


# db = firestore.client()


# def get_comunas():
#     return db.collection('comunas').get()