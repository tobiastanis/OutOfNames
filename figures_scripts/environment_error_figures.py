import matplotlib.pyplot as plt
import numpy as np
from Estimation_Model.Executor import t
from Estimation_Model.Executor import x_error


env_pos_error_eml2o = np.linalg.norm(x_error[:, 0:3], axis=1)
env_vel_error_eml2o = np.linalg.norm(x_error[:, 3:6], axis=1)
env_pos_error_elo = np.linalg.norm(x_error[:, 6:9], axis=1)
env_vel_error_elo = np.linalg.norm(x_error[:, 9:12], axis=1)

print(max(env_pos_error_eml2o))
print(max(env_vel_error_eml2o))
print(max(env_pos_error_elo))
print(max(env_vel_error_elo))

fig1, (ax1, ax2) = plt.subplots(2, 1, constrained_layout=False, sharey=False)
ax1.plot(t, env_pos_error_eml2o)
ax1.set_xlabel('Time [days]')
ax1.set_ylabel('3D-position error [m]')
ax1.set_title('Environment states position error')
ax1.set_xlim(0, 14)
ax2.plot(t, env_vel_error_eml2o)
ax2.set_xlabel('Time [days]')
ax2.set_ylabel('3D-velocity error [m/s]')
ax2.set_title('Moon-centered trajectories in xz-plane')
ax2.set_xlim(0, 14)


fig2, (ax1, ax2) = plt.subplots(2, 1, constrained_layout=False, sharey=False)
ax1.plot(t, env_pos_error_elo)
ax1.set_xlabel('Time [days]')
ax1.set_ylabel('3D-position error [m]')
ax1.set_title('Environment states position error')
ax2.plot(t, env_vel_error_elo)
ax2.set_xlabel('Time [days]')
ax2.set_ylabel('3D-velocity error [m/s]')
ax2.set_title('Moon-centered trajectories in xz-plane')

plt.show()