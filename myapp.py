import dropbox
access_token = '=sl.A8OmJb6Y_9idMBTuLkNfqMTtKCUn90TAoA-p9veqb9h5wA6UcdZC7zrO_xf44wXxGxinsHpa5EnAp_AbpE--RZMSAqmhoCcYWdsFHz3D9Jc7K1qGcd9jKnGVfkLYhjV83BDqK-w'
file_from = 'F:\PyCharm\WebScraping\Library\KDL.ipynb'
file_to = 'https://www.dropbox.com/home/KDLLibraryScrape'
def upload_file(file_from, file_to):
    dbx = dropbox.Dropbox(access_token)
    f = open(file_from, 'rb')
    dbx.files_upload(f.read(), file_to)
upload_file(file_from,file_to)