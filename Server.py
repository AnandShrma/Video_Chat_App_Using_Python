{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2,socket,pickle,struct"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "s=socket.socket()\n",
    "socket_addr=(\"localhost\",9999)\n",
    "s.bind(socket_addr)\n",
    "s.listen(5)\n",
    "while True:\n",
    "    c,addr=s.accept()\n",
    "    if c:\n",
    "        vid=cv2.VideoCapture(0)\n",
    "        try:\n",
    "            while(vid.isOpened()):\n",
    "                img,frame=vid.read()\n",
    "                a=pickle.dumps(frame)\n",
    "                message=struct.pack(\"Q\",len(a))+a\n",
    "                c.sendall(message)\n",
    "                cv2.imshow('TRANSMITTING VIDEO',frame)\n",
    "                if cv2.waitKey(1)==13:\n",
    "                    break\n",
    "        except:\n",
    "            print('connection interrupted')\n",
    "            break\n",
    "    break\n",
    "cv2.destroyAllWindows()\n",
    "c.close()\n",
    "vid.release()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
0 comments on commit 51e151a