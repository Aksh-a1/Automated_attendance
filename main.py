import kairos_face as kf

def auth():
    #kairos api id and key
    kf.settings.app_id = ''
    kf.settings.app_key = ''


def enroll(image,id,gname):
    '''Takes three arguments image=image_path, id=subject_id and gname=gallery_name'''
    # Enrolling from a URL
    # kf.enroll_face(url='', subject_id='sub', gallery_name='test')
    # Enrolling from a file
    #passing image_path of the image which is to be enrolled, subject_id: name from which it should be enrolled, gallery_name: in which gallery it shoud be enrolled
    kf.enroll_face(file=image, subject_id=id, gallery_name=gname)


def recog(image):
    '''Takes only one argument image=image_path'''
    # Recognizing from an URL
    # recognized_faces = kf.recognize_face(url='', gallery_name='test')
    # Recognizing from a file
    #passing image_path of the image which is to be recognized, gallery _name: to search in which gallery, threshold: confidence value, only give success result for match above this level
    recognized_faces = kf.recognize_face(file=image, gallery_name='test', additional_arguments={"threshold":"0.50"})
    print(recognized_faces)


def remo(id,gname):
    '''Takes two arguments,gname=gallery_name from where to be deleted and id=subject_id to be deleted'''
    #passing subject_id to be deleted and gallery_name from where it will be deleted.
    kf.remove_face(subject_id=id, gallery_name=gname)

def remog(gname):
    '''Takes argument gname=gallery_name to be deleted'''
    #passing gallery_name to be deleted
    remove_gallery = kf.remove_gallery(gname)

def galldet():
    '''Takes no argument. Gives details of all the galleries present'''
    #getting a list of all galleries here
    galleries_object = kf.get_galleries_names_object()

    #iterating every gallery
    for gallery_name in galleries_object:
        #extracting name and subjects of gallery from gallery_name
        gallery = kf.get_gallery_object(gallery_name)
        print('Gallery name: {}'.format(gallery.name))
        print('Gallery subjects: {}'.format(gallery.subjects))



while True:
    n=int(input("\n1.) Enroll a face\n2.) Recognize a face\n3.)Get gallery details\n4.)Remove a subject\n5.)Remove a galery\n6.)Exit\n"))
    if n==1:
        #directory where all the faces are present
        dir='faces/'
        #enrolling every face present in the directory
        for i in range(1,9):
            fn = dir+str(i)+'.jpg'
            id = str(input("Subject id: "))
            # gname = str(input("Gallery Name: "))
            auth()
            enroll(fn,id,gname = 'test')
    if n==2:
        auth()
        fn = 'ja.jpg'
        recog(fn)
    if n==3:
        auth()
        galldet()
    if n==4:
        gname = str(input("Enter the gallery name from which you want to delete: "))
        id = str(input("Enter the subject_id you want to delete: "))
        auth()
        remo(id,gname)
    if n==5:
        auth()
        remog()
    if n==6:
        quit()
