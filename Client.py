{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import socket,cv2,struct,pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "c=socket.socket()\n",
    "c.connect(('localhost',9999))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "data=b\"\"\n",
    "payload_size=struct.calcsize(\"Q\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "while True:\n",
    "    while len(data)<payload_size:\n",
    "        packet=c.recv(4*1024)\n",
    "        if not packet: break\n",
    "        data+=packet\n",
    "    packed_msg_size=data[:payload_size]\n",
    "    data=data[payload_size:]\n",
    "    msg_size=struct.unpack(\"Q\",packed_msg_size)[0]\n",
    "    try:\n",
    "        while len(data) <msg_size:\n",
    "            data+=c.recv(4*1024)\n",
    "        frame_data=data[:msg_size]\n",
    "        data = data[msg_size:]\n",
    "        frame=pickle.loads(frame_data)\n",
    "        cv2.imshow(\"RECEIVING VIDEO\",frame)\n",
    "        if cv2.waitKey(1)==13:\n",
    "            break\n",
    "    except:\n",
    "        print('connection interrupted')\n",
    "        break\n",
    "cv2.destroyAllWindows()\n",
    "c.close()\n",
    "        "
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
