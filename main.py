import kairos_face as kf

def auth():
    kf.settings.app_id = ''
    kf.settings.app_key = ''


def enroll(image,id,gname):
    # Enrolling from a URL
    # kf.enroll_face(url='', subject_id='sub', gallery_name='test')
    # Enrolling from a file
    kf.enroll_face(file=image, subject_id=id, gallery_name=gname)


def recog(image):
    # Recognizing from an URL
    # recognized_faces = kf.recognize_face(url='', gallery_name='test')
    # Recognizing from a file
    recognized_faces = kf.recognize_face(file=image, gallery_name='test', additional_arguments={"threshold":"0.50"})
    print(recognized_faces)


def remo():
    kf.remove_face(subject_id='sub', gallery_name='test')

def remog():
    remove_gallery = kf.remove_gallery('test')

def galldet():
    galleries_object = kf.get_galleries_names_object()

    for gallery_name in galleries_object:
        gallery = kf.get_gallery_object(gallery_name)
        print('Gallery name: {}'.format(gallery.name))
        print('Gallery subjects: {}'.format(gallery.subjects))



while True:
    n=int(input("\n1.) Enroll a face\n2.) Recognize a face\n3.)Get gallery details\n4.)Remove a subject\n5.)Remove a galery\n6.)Exit\n"))
    if n==1:
        dir='faces/'
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
        pass
    if n==5:
        auth()
        remog()
    if n==6:
        quit()
