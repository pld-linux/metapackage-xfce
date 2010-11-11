Summary:	Xfce desktop environment
Summary(pl.UTF-8):	Środowisko graficzne Xfce
Name:		metapackage-xfce
Version:	4.6.1
Release:	2
License:	GPL
Group:		X11/Applications
Requires:	Terminal >= 0.2.12
Requires:	Thunar >= 1.0.1
Requires:	gtk-xfce-engine >= 2.6.0
Requires:	mousepad >= 0.2.16
Requires:	orage >= 4.6.1
Requires:	xfce-preferred-applications >= 0.3.101
Requires:	xfce-utils >= 4.6.1
Requires:	xfce4-appfinder >= 4.6.1
Requires:	xfce4-icon-theme >= 4.4.3
Requires:	xfce4-mixer >= 4.6.1
Requires:	xfce4-panel >= 4.6.1
Requires:	xfce4-session >= 4.6.1
Requires:	xfce4-settings >= 4.6.1
Requires:	xfconf >= 4.6.1
Requires:	xfdesktop >= 4.6.1
Requires:	xfprint >= 4.6.1
Requires:	xfwm4 >= 4.6.1
Requires:	xfwm4-themes >= 4.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xfce desktop environment metapackage.

%description -l pl.UTF-8
Metapakiet środowiska graficznego Xfce.

%package extras
Summary:	Additional packages for Xfce desktop environment
Summary(pl.UTF-8):	Dodatkowe pakiety dla środowiska graficznego Xfce
Group:		X11/Applications
Requires:	Thunar-volman >= 0.3.80
Requires:	Xarchiver >= 0.5.2
Requires:	ristretto >= 0.0.21
Requires:	xfburn >= 0.4.1
Requires:	xfce4-artwork >= 0.1
Requires:	xfce4-power-manager >= 0.6.2
Requires:	xfce4-taskmanager >= 0.4.1
Requires:	xfmedia >= 0.9.2
Requires:	xfmedia-plugins >= 0.9.2

%description extras
Metapackage to install additional packages for Xfce desktop
environment.

%description extras -l pl.UTF-8
Metapakiet instalujący dodatkowe pakiety dla środowiska graficznego
Xfce.

%package panel-plugins
Summary:	Panel plugins for Xfce desktop environment
Summary(pl.UTF-8):	Wtyczki panelu środowiska graficznego Xfce
Group:		X11/Applications
Requires:	xfce4-battery-plugin >= 0.5.1
Requires:	xfce4-cellmodem-plugin >= 0.0.5
Requires:	xfce4-clipman-plugin >= 0.9.0
Requires:	xfce4-cpufreq-plugin >= 0.0.1
Requires:	xfce4-cpugraph-plugin >= 0.4.0
Requires:	xfce4-datetime-plugin >= 0.6.1
Requires:	xfce4-diskperf-plugin >= 2.2.0
Requires:	xfce4-eyes-plugin >= 4.4.0
Requires:	xfce4-fsguard-plugin >= 0.4.2
Requires:	xfce4-genmon-plugin >= 3.0
Requires:	xfce4-mount-plugin >= 0.5.5
Requires:	xfce4-mpc-plugin >= 0.3.3
Requires:	xfce4-netload-plugin >= 0.4.0
Requires:	xfce4-notes-plugin >= 1.6.4
Requires:	xfce4-places-plugin >= 1.1.0
Requires:	xfce4-playercontrol-plugin >= 0.3.0
Requires:	xfce4-quicklauncher-plugin >= 1.9.4
Requires:	xfce4-radio-plugin >= 0.4.1
Requires:	xfce4-sensors-plugin >= 0.10.99.3
Requires:	xfce4-smartbookmark-plugin >= 0.4.2
Requires:	xfce4-systemload-plugin >= 0.4.2
Requires:	xfce4-time-out-plugin >= 0.1.1
Requires:	xfce4-timer-plugin >= 0.6.1
Requires:	xfce4-trigger-launcher >= 4.2.4.1
Requires:	xfce4-verve-plugin >= 0.3.6
Requires:	xfce4-wavelan-plugin >= 0.5.4
Requires:	xfce4-weather-plugin >= 0.6.2
Requires:	xfce4-xfapplet-plugin >= 0.1.0
Requires:	xfce4-xkb-plugin >= 0.5.3.2

%description panel-plugins
Metapackage to install panel plugins for Xfce desktop environment.

%description panel-plugins -l pl.UTF-8
Metapakiet instalujący wtyczki panelu środowiska graficznego Xfce.

%package thunar-plugins
Summary:	Plugins for Thunar file manager
Summary(pl.UTF-8):	Wtyczki do zarządcy plików Thunar
Group:		X11/Applications
Requires:	Thunar-archive-plugin >= 0.2.4
Requires:	Thunar-media-tags-plugin >= 0.1.2
Requires:	Thunar-thumbnailers >= 0.4.1

%description thunar-plugins
Plugins for Thunar file manager.

%description thunar-plugins -l pl.UTF-8
Wtyczki do zarządcy plików Thunar.

%prep

%files
%files extras
%files panel-plugins
%files thunar-plugins
