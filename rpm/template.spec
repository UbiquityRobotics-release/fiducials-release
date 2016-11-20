Name:           ros-kinetic-fiducial-detect
Version:        0.1.1
Release:        0%{?dist}
Summary:        ROS fiducial_detect package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-cv-bridge
Requires:       ros-kinetic-image-transport
Requires:       ros-kinetic-orocos-kdl
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-tf2
Requires:       ros-kinetic-tf2-geometry-msgs
Requires:       ros-kinetic-tf2-ros
Requires:       ros-kinetic-visualization-msgs
BuildRequires:  opencv-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cv-bridge
BuildRequires:  ros-kinetic-fiducial-lib
BuildRequires:  ros-kinetic-fiducial-pose
BuildRequires:  ros-kinetic-image-transport
BuildRequires:  ros-kinetic-orocos-kdl
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-tf2
BuildRequires:  ros-kinetic-tf2-geometry-msgs
BuildRequires:  ros-kinetic-tf2-ros
BuildRequires:  ros-kinetic-visualization-msgs

%description
The fiducials_ros package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sat Nov 19 2016 Jim Vaughan <jimv@mrjim.com> - 0.1.1-0
- Autogenerated by Bloom

