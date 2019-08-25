Summary:	Xfce desktop environment
Summary(pl.UTF-8):	Środowisko graficzne Xfce
Name:		metapackage-xfce
Version:	4.14.0
Release:	2
License:	GPL
Group:		X11/Applications
Requires:	catfish >= 1.4.9
Requires:	exo >= 0.12.8
Requires:	garcon >= 0.6.4
Requires:	libxfce4ui >= 4.14.0
Requires:	libxfce4util >= 4.14.0
Requires:	mousepad >= 0.4.2
Requires:	orage >= 4.12.1
Requires:	Thunar >= 1.8.9
Requires:	Thunar-volman >= 0.9.5
Requires:	tumbler >= 0.2.7
Requires:	xfce4-appfinder >= 4.14.0
Requires:	xfce4-mixer >= 4.11.0-8
Requires:	xfce4-notifyd >= 0.4.4
Requires:	xfce4-panel >= 4.14.0
Requires:	xfce4-panel-profiles >= 1.0.9
Requires:	xfce4-power-manager >= 1.6.5
Requires:	xfce4-session >= 4.14.0
Requires:	xfce4-settings >= 4.14.0
Requires:	xfce4-terminal >= 0.8.8
Requires:	xfce4-volumed >= 0.1.13-7
Requires:	xfce-preferred-applications >= 0.12.8
Requires:	xfconf >= 4.14.0
Requires:	xfdesktop >= 4.14.0
Requires:	xfprint >= 4.6.1-16
Requires:	xfwm4 >= 4.14.0
Requires:	xfwm4-themes >= 4.10.0
Requires:	xfce4-screensaver >= 0.1.8
Obsoletes:	gtk-xfce-engine
Obsoletes:	xfce4-kbdleds-plugin
Obsoletes:	xfce4-linelight-plugin
Obsoletes:	xfce4-lock-keys-plugin
Obsoletes:	xfce4-playercontrol-plugin
Obsoletes:	xfce4-radio-plugin
Obsoletes:	xfce4-taskbar-plugin
Obsoletes:	xfce4-trigger-launcher
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
Requires:	ristretto >= 0.10.0
Requires:	xfburn >= 0.5.5-2
Requires:	xfce4-dict >= 0.8.2
Requires:	xfce4-screenshooter >= 1.9.5
Requires:	xfce4-taskmanager >= 1.2.2-2
Suggests:	gigolo >= 0.5.0
Suggests:	parole >= 1.0.4
Suggests:	xfdashboard >= 0.7.5-3
Suggests:	xfmpc >= 0.3.0

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
Requires:	xfce4-cellmodem-plugin >= 0.0.5
Requires:	xfce4-clipman-plugin >= 1.4.3
Requires:	xfce4-cpufreq-plugin >= 1.2.1
Requires:	xfce4-cpugraph-plugin >= 1.1.0
Requires:	xfce4-datetime-plugin >= 0.8.0
Requires:	xfce4-dict-plugin >= 0.8.2
Requires:	xfce4-diskperf-plugin >= 2.6.2
Requires:	xfce4-embed-plugin >= 1.6.0
Requires:	xfce4-eyes-plugin >= 4.5.0
Requires:	xfce4-fsguard-plugin >= 1.1.1
Requires:	xfce4-genmon-plugin >= 4.0.2
Requires:	xfce4-indicator-plugin >= 2.3.4-3
Requires:	xfce4-mailwatch-plugin >= 1.2.0-6
Requires:	xfce4-mount-plugin >= 1.1.3
Requires:	xfce4-mpc-plugin >= 0.5.2
Requires:	xfce4-netload-plugin >= 1.3.2
Requires:	xfce4-notes-plugin >= 1.8.1-3
Requires:	xfce4-places-plugin >= 1.8.1
Requires:	xfce4-pulseaudio-plugin >= 0.4.2
Requires:	xfce4-quicklauncher-plugin >= 1.9.4-9
Requires:	xfce4-sensors-plugin >= 1.3.92
Requires:	xfce4-smartbookmark-plugin >= 0.5.1
Requires:	xfce4-statusnotifier-plugin >= 0.2.1
Requires:	xfce4-systemload-plugin >= 1.2.3
Requires:	xfce4-time-out-plugin >= 1.0.3
Requires:	xfce4-timer-plugin >= 1.7.0
Requires:	xfce4-verve-plugin >= 2.0.0
Requires:	xfce4-wavelan-plugin >= 0.6.1
Requires:	xfce4-weather-plugin >= 0.10.0
Requires:	xfce4-whiskermenu-plugin >= 2.3.3
Requires:	xfce4-windowck-plugin >= 0.4.6-2
Requires:	xfce4-xkb-plugin >= 0.8.1

%description panel-plugins
Metapackage to install panel plugins for Xfce desktop environment.

%description panel-plugins -l pl.UTF-8
Metapakiet instalujący wtyczki panelu środowiska graficznego Xfce.

%package thunar-plugins
Summary:	Plugins for Thunar file manager
Summary(pl.UTF-8):	Wtyczki do zarządcy plików Thunar
Group:		X11/Applications
Requires:	Thunar-archive-plugin >= 0.4.0-4
Requires:	Thunar-media-tags-plugin >= 0.3.0-4

%description thunar-plugins
Plugins for Thunar file manager.

%description thunar-plugins -l pl.UTF-8
Wtyczki do zarządcy plików Thunar.

%prep

%files
%files extras
%files panel-plugins
%files thunar-plugins
