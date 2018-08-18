
        navigator.getUserMedia = ( navigator.getUserMedia ||
                           navigator.webkitGetUserMedia ||
                           navigator.mozGetUserMedia ||
                           navigator.msGetUserMedia);

    var video;
    var webcamStream;


    function stopWebcam() {
        webcamStream.stop();
    }

    var canvas, ctx;

    function init() {
      // Get the canvas and obtain a context for
      // drawing in it
      canvas = document.getElementById("myCanvas");
      ctx = canvas.getContext('2d');

      if (navigator.getUserMedia) {
         navigator.getUserMedia (

            // constraints
            {
               video: {width: 480, height: 480},
               audio: false
            },

            // successCallback
            function(localMediaStream) {
                video = document.querySelector('video');
               video.src = window.URL.createObjectURL(localMediaStream);
               webcamStream = localMediaStream;
            },

            // errorCallback
            function(err) {
               console.log("The following error occured: " + err);
            }
         );
      } else {
         console.log("getUserMedia not supported");
      }
    }


    //Add file blob to form and post
    function postFile(file) {
        let formdata = new FormData();
        formdata.append("image", file);
        let xhr = new XMLHttpRequest();
        xhr.open('POST', 'http://attendance.localtunnel.me/image', true);
        xhr.onload = function () {
            if (this.status === 200)
                console.log(this.response);
            else
                console.error(xhr);
        };
        xhr.send(formdata);
    }

    function snapshot() {
       // Draws current image from the video element into the canvas
      ctx.drawImage(video, 0,0, canvas.width, canvas.height);
      canvas.toBlob(postFile, 'image/jpeg');
      var el = document.getElementById("button1");
      if (el.value=="Capture Image") el.value = "Recapture";
    }
