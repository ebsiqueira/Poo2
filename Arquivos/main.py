import leituraAPI
import matplotlib.pyplot as plt

plt.subplot(2, 2, 1)
leituraAPI.callAPI('apiAAPL.json')
plt.subplot(2, 2, 2)
leituraAPI.callAPI('apiGOGL.json')
plt.subplot(2, 2, 3)
leituraAPI.callAPI('apiMSFT.json')
plt.subplot(2, 2, 4)
leituraAPI.callAPI('apiVALE.json')
plt.show()

