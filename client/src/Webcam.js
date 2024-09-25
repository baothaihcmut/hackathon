import React, { useRef } from 'react';
import Webcam from 'react-webcam';
import { io } from 'socket.io-client';


const socket = io('localhost:8000', {
    path: '/sockets',
  });

const WebcamCapture = () => {
    const webRef = useRef(null);
    const captureImage = () => {
        const img = webRef.current.getScreenshot()
        console.log(img.image)
        socket.emit('capture', {data: img})
    }
    return (
        <div>
            React Webcam 
            <Webcam ref={webRef} screenshotFormat='image/jpeg' />
            <button onClick={()=>{
                captureImage()
            }}>Capture image </button>
        </div>
    )
};

export default WebcamCapture;
