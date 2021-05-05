import matplotlib.pyplot as plt, numpy as np
from mpl_toolkits.mplot3d import proj3d
import pandas as pd

X_CFRP = [1165.30815, 1165.30912, 1165.31301, 1165.31447, 1165.31508, 1185.25878, 1185.25916, 1185.2595, 1185.25836, 1185.25787, 1185.25338, 1185.25432, 1265.06628, 1284.97514, 1290.08889, 1310.20498, 1349.59954, 1369.34604, 1389.09218, 1408.83813, 1308.9219, 1290.94436, 1277.63054, 1259.91663, 1266.07709, 1266.05537, 1286.65732, 1289.2725, 1271.37698, 1242.1715, 1240.05171, 1207.45563, 1374.96039, 1411.84573, 1382.34868, 1355.87252, 1363.18574, 1345.45039, 1335.67884, 1325.80043, 1396.24601, 1382.07438, 1368.14125, 1353.96908, 1325.8631, 1290.44425, 1271.60327, 1293.64546, 1279.76782, 1166.28317, 1166.28479, 1209.01299, 1209.01337, 1186.34413, 1186.34494, 1209.01378, 1209.01413, 1245.15544, 1245.15578, 1245.15493, 1245.1546, 1207.48736, 1207.45542, 1207.48661, 1207.45518, 1306.15013, 1313.79135, 1245.15611, 1309.87362, 1245.14281, 1427.12077, 1245.15464, 1245.15632, 1428.5769]
Y_CFRP = [-488.587077, -467.709054, -370.074317, -324.172028, -301.205387, -318.839408, -298.367717, -277.889032, -339.303376, -359.758836, -509.108272, -482.283205, -487.975, -485.13755, -465.181169, -469.793714, -465.629997, -465.292233, -464.954365, -464.616607, -363.576327, -323.144909, -299.294255, -291.741477, -317.122474, -337.287771, -343.193846, -363.912485, -356.360638, -299.891799, -276.952244, -298.299271, -385.535344, -402.98682, -403.492067, -384.220641, -403.820187, -403.626808, -384.566311, -403.963079, -428.812818, -443.178639, -429.294069, -443.659785, -444.140726, -385.34023, -404.890026, -444.691756, -430.805946, -446.374753, -406.989865, -458.945539, -434.547909, -434.934943, -404.310921, -403.92382, -375.19768, -400.75135, -373.819342, -436.865218, -458.37401, -507.727354, -321.078802, -488.144998, -343.848932, -404.299253, -384.94085, -343.375847, -430.291138, -487.502186, -428.706299, -507.083943, -322.403658, -393.883745]
Z_CFRP = [-800.178986, -802.712165, -812.801547, -816.603349, -818.293463, -812.251941, -813.737774, -815.115751, -810.655893, -808.947191, -792.7787, -796.187038, -776.370153, -771.952089, -773.144563, -767.77518, -758.823889, -754.126308, -749.42717, -744.726406, -779.070096, -786.694836, -791.630143, -796.383904, -793.092295, -791.529191, -786.12619, -783.739195, -788.672598, -800.053546, -802.108353, -808.448797, -761.262142, -750.72801, -757.748295, -765.957301, -762.307214, -766.574736, -770.759258, -771.246608, -751.793871, -753.618884, -758.481475, -760.305292, -766.988599, -781.510007, -784.124241, -774.64559, -779.489171, -804.927678, -809.084785, -793.284063, -796.012552, -801.389583, -804.56047, -799.183423, -801.90865, -790.858336, -793.400012, -787.116919, -784.701421, -787.635299, -806.787388, -790.140716, -804.988976, -775.91702, -775.962187, -796.026389, -772.336156, -781.203066, -744.398016, -778.694079, -797.687924, -747.612655]
X = [1207.44147, 1410.1786, 1329.99025, 1428.58334, 1268.19269, 1165.30713, 1165.31561, 1165.31378, 1272.15428, 1307.31481, 1328.58859, 1397.15003, 1340.03548, 1270.43461, 1270.63098, 1189.84425, 1190.53149]
Y = [-278.515801, -442.697295, -465.986615, -464.300478, -507.691584, -509.448651, -278.229836, -347.128714, -276.403018, -343.561498, -362.381232, -391.3314, -429.775126, -448.754634, -382.335328, -454.435864, -383.716322]
Z = [-809.786048, -746.929475, -763.484675, -740.021598, -773.090817, -797.508938, -819.847555, -814.773865, -794.48221, -781.15811, -774.470757, -755.393048, -765.1661, -779.747871, -786.529189, -798.386493, -805.538976]
Name = ['SK-SPLDOR-FCFC-4.8-abs0873B3E5.2051', 'SK-SPLDOR-FCFC-4.8-abs0873B3E5.2052', 'SK-SPLDOR-FCFC-4.8-abs0873B3E5.2053', 'SK-SPLDOR-FCFC-4.8-abs0873B3E5.2054', 'SK-SPLDOR-FCFC-4.8-abs0873B3E5.2055', 'SK-SPLDOR-FCFC-4.8-abs0873B3E5.2056', 'SK-SPLDOR-FCFC-4.8-abs0873B3E5.2057', 'SK-SPLDOR-FCFC-4.8-abs0873B3E5.2058', 'SK-SPLDOR-FCFC-4.8-abs0873B3E5.2059', 'SK-SPLDOR-FCFC-4.8-abs0873B3E5.2060', 'SK-SPLDOR-FCFC-4.8-abs0873B3E5.2061', 'SK-SPLDOR-FCFC-4.8-abs0873B3E5.2062', 'SK-SPLDOR-FCFC-4.8-abs0873B3E5.2063', 'SK-SPLDOR-FCFC-4.8-abs0873B3E5.2064', 'SK-SPLDOR-FCFC-4.8-abs0873B3E5.2065', 'SK-SPLDOR-FCFC-4.8-abs0873B3E5.2066', 'SK-SPLDOR-FCFC-4.8-abs0873B3E5.2067', 'SK-SPLDOR-FCFC-4.8-abs0873B3E5.2068', 'SK-SPLDOR-FCFC-4.8-abs0873B3E5.2069', 'SK-SPLDOR-FCFC-4.8-abs0873B3E5.2070', 'SK-SPLDOR-FCFC-4.8-abs0873B3E5.2192', 'SK-SPLDOR-FCFC-4.8-abs0873B3E5.2193', 'SK-SPLDOR-FCFC-4.8-abs0873B3E5.2194', 'SK-SPLDOR-FCFC-4.8-abs0873B3E5.2195', 'SK-SPLDOR-FCFC-4.8-abs0873B3E5.2196', 'SK-SPLDOR-FCFC-4.8-abs0873B3E5.2197', 'SK-SPLDOR-FCFC-4.8-abs0873B3E5.2198', 'SK-SPLDOR-FCFC-4.8-abs0873B3E5.2199', 'SK-SPLDOR-FCFC-4.8-abs0873B3E5.2200', 'SK-SPLDOR-FCFC-4.8-abs0873B3E5.2201', 'SK-SPLDOR-FCFC-4.8-abs0873B3E5.2202', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E6.2327', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E8.2487', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E8.2488', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E8.2489', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E8.2490', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E8.2491', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E8.2492', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E8.2493', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E8.2494', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E8.2496', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E8.2497', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E8.2498', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E8.2499', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E8.2500', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E9.2529', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E9.2530', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E9.2531', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E9.2532', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E9.2557', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E9.2558', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E10.2561', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E10.2562', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E10.2563', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E10.2564', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E10.2565', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E10.2566', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E10.2567', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E10.2568', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E10.2569', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E10.2570', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E7.2633', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E7.2634', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E8.2677', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E8.2678', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E9.2679', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E8.2680', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E8.2681', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E8.2682', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E8.2683', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E8.2744', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E7.2931', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E7.2932', 'SK-SPLDOR-DOFR-FCFCFC-4.8-abs0873B3E8.3178']
IDs = [2051, 2052, 2053, 2054, 2055, 2056, 2057, 2058, 2059, 2060, 2061, 2062, 2063, 2064, 2065, 2066, 2067, 2068, 2069, 2070, 2192, 2193, 2194, 2195, 2196, 2197, 2198, 2199, 2200, 2201, 2202, 2327, 2487, 2488, 2489, 2490, 2491, 2492, 2493, 2494, 2496, 2497, 2498, 2499, 2500, 2529, 2530, 2531, 2532, 2557, 2558, 2561, 2562, 2563, 2564, 2565, 2566, 2567, 2568, 2569, 2570, 2633, 2634, 2677, 2678, 2679, 2680, 2681, 2682, 2683, 2744, 2931, 2932, 3178]

CFRP = pd.DataFrame({'X': X_CFRP, 'Y': Y_CFRP, 'Z': Z_CFRP}).to_numpy()
NO_CFRP = pd.DataFrame({'X': X, 'Y': Y, 'Z': Z}).to_numpy()

def visualize3DData(A, B, Name, IDs):
    """Visualize data in 3d plot with popover next to mouse position"""

    fig = plt.figure(figsize=(16, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(A[:, 0], A[:, 1], A[:, 2], color='red', depthshade=False, picker=True)
    ax.scatter(B[:, 0], B[:, 1], B[:, 2], color='blue', depthshade=False, picker=True)

    def distance(point, event):
        """Return distance between mouse position and given data point

        Args:
            point (np.array): np.array of shape (3,), with x,y,z in data coords
            event (MouseEvent): mouse event (which contains mouse position in .x and .xdata)
        Returns:
            distance (np.float64): distance (in screen coords) between mouse pos and data point
        """
        assert point.shape == (3,), "distance: point.shape is wrong: %s, must be (3,)" % point.shape

        # Project 3d data space to 2d data space
        x2, y2, _ = proj3d.proj_transform(point[0], point[1], point[2], plt.gca().get_proj())
        # Convert 2d data space to 2d screen space
        x3, y3 = ax.transData.transform((x2, y2))

        return np.sqrt((x3 - event.x) ** 2 + (y3 - event.y) ** 2)

    def calcClosestDatapoint(A, event):
        """"Calculate which data point is closest to the mouse position.

        Args:
            A (np.array) - array of points, of shape (numPoints, 3)
            event (MouseEvent) - mouse event (containing mouse position)
        Returns:
            smallestIndex (int) - the index (into the array of points A) of the element closest to the mouse position
        """
        distances = [distance(A[i, 0:3], event) for i in range(A.shape[0])]
        return np.argmin(distances)

    def annotatePlot(A, index):
        """Create popover label in 3d chart

        Args:
            A (np.array) - array of points, of shape (numPoints, 3)
            index (int) - index (into points array A) of item which should be printed
        Returns:
            None
        """
        # If we have previously displayed another label, remove it first
        if hasattr(annotatePlot, 'label'):
            annotatePlot.label.remove()
        # Get data point from array of points X, at position index
        x2, y2, _ = proj3d.proj_transform(A[index, 0], A[index, 1], A[index, 2], ax.get_proj())
        annotatePlot.label = plt.annotate("Name {}\n ID {}".format(Name[index], IDs[index]),
                                          xy=(x2, y2), xytext=(-20, 20), textcoords='offset points', ha='right',
                                          va='bottom',
                                          bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
                                          arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
        fig.canvas.draw()

    def onMouseMotion(event):
        """Event that is triggered when mouse is moved. Shows text annotation over data point closest to mouse."""
        closestIndex = calcClosestDatapoint(A, event)
        annotatePlot(A, closestIndex)

    fig.canvas.mpl_connect('motion_notify_event', onMouseMotion)  # on mouse motion
    plt.show()


if __name__ == '__main__':
    A = CFRP
    B = NO_CFRP
    visualize3DData(A, B, Name, IDs)

