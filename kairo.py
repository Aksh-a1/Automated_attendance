import kairos_face as kf

#kairos api id and key
kf.settings.app_id = '22feceff'
kf.settings.app_key = '76c3dcdbb5c93432712f448c4b940c77'


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
    recognized_faces = kf.recognize_face(file=image, gallery_name='student', additional_arguments={"threshold":"0.50"})
    return recognized_faces


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
