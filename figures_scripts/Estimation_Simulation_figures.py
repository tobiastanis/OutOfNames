import matplotlib.pyplot as plt
from Estimation_Model.Executor import stdP
from Estimation_Model.Executor import t
from Estimation_Model.Executor import x_error
from Estimation_Model.Executor import visibility
from Estimation_Model.Executor import X
from Measurement_Model.Nominal_Observations_Cooker import states

std_Pk_up = 3*stdP
std_Pk_down =-3*stdP

"""
fig1, (ax1, ax2, ax3) = plt.subplots(3, 1, constrained_layout=True, sharey=True)
ax1.plot(t, states[:, 0], color='blue', label='Nominal')
ax1.plot(t, X[:, 0], color='red', label='Estimated')
ax2.plot(t, states[:, 1], color='blue')
ax2.plot(t, X[:, 1], color='red')
ax3.plot(t, states[:, 2], color='blue')
ax3.plot(t, X[:, 2], color='red')
ax1.legend()

fig2, (ax1, ax2, ax3) = plt.subplots(3, 1, constrained_layout=True, sharey=True)
ax1.plot(t, states[:, 3], color='blue', label='Nominal')
ax1.plot(t, X[:, 3], color='red', label='Estimated')
ax2.plot(t, states[:, 4], color='blue')
ax2.plot(t, X[:, 4], color='red')
ax3.plot(t, states[:, 5], color='blue')
ax3.plot(t, X[:, 5], color='red')
ax1.legend()

fig3, (ax1, ax2, ax3) = plt.subplots(3, 1, constrained_layout=True, sharey=True)
ax1.plot(t, states[:, 6], color='blue', label='Nominal')
ax1.plot(t, X[:, 6], color='red', label='Estimated')
ax2.plot(t, states[:, 7], color='blue')
ax2.plot(t, X[:, 7], color='red')
ax3.plot(t, states[:, 8], color='blue')
ax3.plot(t, X[:, 8], color='red')
ax1.legend()

fig4, (ax1, ax2, ax3) = plt.subplots(3, 1, constrained_layout=True, sharey=True)
ax1.plot(t, states[:, 9], color='blue', label='Nominal')
ax1.plot(t, X[:, 9], color='red', label='Estimated')
ax2.plot(t, states[:, 10], color='blue')
ax2.plot(t, X[:, 10], color='red')
ax3.plot(t, states[:, 11], color='blue')
ax3.plot(t, X[:, 11], color='red')
ax1.legend()
"""


plt.figure()
plt.plot(t, x_error[:, 0], color='red', label='x')
plt.plot(t, x_error[:, 1], color='blue', label='y')
plt.plot(t, x_error[:, 2], color='green', label='z')

plt.plot(t, std_Pk_up[:, 0], color='red', linestyle='-.' , label='3$\sigma_{x}$')
plt.plot(t, std_Pk_down[:, 0], color='red', linestyle='-.')
plt.plot(t, std_Pk_up[:, 1], color='blue', linestyle='-.', label='3$\sigma_{y}$')
plt.plot(t, std_Pk_down[:, 1], color='blue', linestyle='-.')
plt.plot(t, std_Pk_up[:, 2], color='green', linestyle='-.', label='3$\sigma_{z}$')
plt.plot(t, std_Pk_down[:, 2], color='green', linestyle='-.')

plt.legend()
plt.xlim(0, 14)
plt.ylim(-8000, 8000)
plt.grid(True, which="both", ls="-")
plt.xlabel('Time since epoch [days]')
plt.ylabel('Estimated position error [m]')
plt.title('EML2O position error')

plt.figure()
plt.plot(t, x_error[:, 3], color='red', label='$\dot{x}$')
plt.plot(t, x_error[:, 4], color='blue', label='$\dot{y}$')
plt.plot(t, x_error[:, 5], color='green', label='$\dot{z}$')
plt.plot(t, std_Pk_up[:, 3], color='red', linestyle='-.', label='3$\sigma_{\dot{x}}$')
plt.plot(t, std_Pk_down[:, 3], color='red', linestyle='-.')
plt.plot(t, std_Pk_up[:, 4], color='blue', linestyle='-.', label='3$\sigma_{\dot{y}}$')
plt.plot(t, std_Pk_down[:, 4], color='blue', linestyle='-.')
plt.plot(t, std_Pk_up[:, 5], color='green', linestyle='-.', label='3$\sigma_{\dot{z}}$')
plt.plot(t, std_Pk_down[:, 5], color='green', linestyle='-.')
plt.legend()
plt.xlim(0, 14)
plt.ylim(-0.05, 0.05)
plt.grid(True, which="both", ls="-")
plt.xlabel('Time since epoch [days]')
plt.ylabel('Estimated velocity error [m/s]')
plt.title('EML2) velocity error')

plt.figure()
plt.plot(t, x_error[:, 6], color='red', label='x')
plt.plot(t, x_error[:, 7], color='blue', label='y')
plt.plot(t, x_error[:, 8], color='green', label='z')

plt.plot(t, std_Pk_up[:, 6], color='red', linestyle='-.', label='3$\sigma_{x}$')
plt.plot(t, std_Pk_down[:, 6], color='red', linestyle='-.')
plt.plot(t, std_Pk_up[:, 7], color='blue', linestyle='-.', label='3$\sigma_{y}$')
plt.plot(t, std_Pk_down[:, 7], color='blue', linestyle='-.')
plt.plot(t, std_Pk_up[:, 8], color='green', linestyle='-.', label='3$\sigma_{z}$')
plt.plot(t, std_Pk_down[:, 8], color='green', linestyle='-.')

plt.legend()
plt.xlim(0, 14)
plt.ylim(-100000, 100000)

plt.grid(True, which="both", ls="-")
plt.xlabel('Time since epoch [days]')
plt.ylabel('Estimated position error [m]')
plt.title('ELO position error')

plt.figure()
plt.plot(t, x_error[:, 9], color='red', label='$\dot{x}$')
plt.plot(t, x_error[:, 10], color='blue', label='$\dot{y}$')
plt.plot(t, x_error[:, 11], color='green', label='$\dot{z}$')

plt.plot(t, std_Pk_up[:, 9], color='red', linestyle='-.', label='3$\sigma_{\dot{x}}$')
plt.plot(t, std_Pk_down[:, 9], color='red', linestyle='-.')
plt.plot(t, std_Pk_up[:, 10], color='blue', linestyle='-.', label='3$\sigma_{\dot{y}}$')
plt.plot(t, std_Pk_down[:, 10], color='blue', linestyle='-.')
plt.plot(t, std_Pk_up[:, 11], color='green', linestyle='-.', label='3$\sigma_{\dot{z}}$')
plt.plot(t, std_Pk_down[:, 11], color='green', linestyle='-.')

plt.legend()
plt.xlim(0, 14)
plt.ylim(-20, 20)
plt.grid(True, which="both", ls="-")
plt.xlabel('Time since epoch [days]')
plt.ylabel('Estimated velocity error [m/s]')
plt.title('ELO velocity error')


plt.figure()
plt.plot(t, visibility)
plt.xlabel('Time [days]')
plt.ylabel('Visibility [0:No, 1:Yes]')
plt.title('Visbility between the satellites')


plt.show()

