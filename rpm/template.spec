Name:           ros-indigo-robot-self-filter
Version:        0.1.30
Release:        1%{?dist}
Summary:        ROS robot_self_filter package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/robot_self_filter
Source0:        %{name}-%{version}.tar.gz

Requires:       assimp
Requires:       bullet-devel
Requires:       ros-indigo-filters
Requires:       ros-indigo-pcl-ros
Requires:       ros-indigo-resource-retriever
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-tf
Requires:       ros-indigo-urdf
Requires:       ros-indigo-visualization-msgs
BuildRequires:  assimp-devel
BuildRequires:  bullet-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-filters
BuildRequires:  ros-indigo-pcl-ros
BuildRequires:  ros-indigo-resource-retriever
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-urdf
BuildRequires:  ros-indigo-visualization-msgs

%description
Filters the robot's body out of point clouds.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Jan 20 2017 Devon Ash <dash@clearpathrobotics.com> - 0.1.30-1
- Autogenerated by Bloom

* Fri Jan 20 2017 Devon Ash <dash@clearpathrobotics.com> - 0.1.30-0
- Autogenerated by Bloom

* Sat Dec 05 2015 Devon Ash <dash@clearpathrobotics.com> - 0.1.29-1
- Autogenerated by Bloom

* Sat Dec 05 2015 Devon Ash <dash@clearpathrobotics.com> - 0.1.29-0
- Autogenerated by Bloom

* Fri Dec 04 2015 Devon Ash <dash@clearpathrobotics.com> - 0.1.28-2
- Autogenerated by Bloom

* Fri Dec 04 2015 Devon Ash <dash@clearpathrobotics.com> - 0.1.28-1
- Autogenerated by Bloom

* Fri Dec 04 2015 Devon Ash <dash@clearpathrobotics.com> - 0.1.28-0
- Autogenerated by Bloom

* Tue Dec 01 2015 Devon Ash <dash@clearpathrobotics.com> - 0.1.27-1
- Autogenerated by Bloom

* Tue Dec 01 2015 Devon Ash <dash@clearpathrobotics.com> - 0.1.27-0
- Autogenerated by Bloom

