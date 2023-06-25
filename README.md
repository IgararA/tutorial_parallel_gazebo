# tutorial_parallel_gazebo
Gazebo中并联机构的添加

主要内容在于URDF文件中的Gazebo标签中

'''XML
  <gazebo>

      <joint name='WheelJointFixed' type='revolute'>
      <pose relative_to='KneelLegRight_Link'>0.120 0 0.0 0 0 0</pose>
      <parent>KneelLegRight_Link</parent>
      <child>Wheel_Link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-2</lower>
          <upper>2</upper>
          <effort>20</effort>
          <velocity>30</velocity>
        </limit>
      </axis>
      <dynamic>
        <friction>0.01</friction>
        <damping>0.01</damping>
      </dynamic>
    </joint>

  </gazebo>
'''
