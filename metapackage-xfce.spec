Summary:	Xfce desktop environment
Summary(pl.UTF-8):	Środowisko graficzne Xfce
Name:		metapackage-xfce
Version:	4.16.0
Release:	3
License:	GPL
Group:		X11/Applications
Requires:	exo >= 4.16.0
Requires:	garcon >= 0.8.0
Requires:	libxfce4ui >= 4.16.0
Requires:	libxfce4util >= 4.16.0
Requires:	mousepad >= 0.5.1
Requires:	Thunar >= 4.16.1
Requires:	Thunar-volman >= 4.16.0
Requires:	tumbler >= 4.16.0
Requires:	xfce4-appfinder >= 4.16.0
Requires:	xfce4-notifyd >= 0.6.2
Requires:	xfce4-panel >= 4.16.0
Requires:	xfce4-panel-profiles >= 1.0.12
Requires:	xfce4-power-manager >= 4.16.0
Requires:	xfce4-pulseaudio-plugin >= 0.4.2
Requires:	xfce4-session >= 4.16.0
Requires:	xfce4-settings >= 4.16.0
Requires:	xfce4-terminal >= 0.8.10
Requires:	xfce4-volumed-pulse >= 0.2.3
Requires:	xfce-preferred-applications >= 4.16.0
Requires:	xfconf >= 4.16.0
Requires:	xfdesktop >= 4.16.0
Requires:	xfwm4 >= 4.16.0
Requires:	xfwm4-themes >= 4.10.0
Requires:	xfce4-screensaver >= 0.1.11
Obsoletes:	gtk-xfce-engine
Obsoletes:	orage < 4.16.0
Obsoletes:	xfce4-cellmodem-plugin < 4.16.0
Obsoletes:	xfce4-embed-plugin < 4.16.0
Obsoletes:	xfce4-kbdleds-plugin < 4.16.0
Obsoletes:	xfce4-linelight-plugin < 4.16.0
Obsoletes:	xfce4-lock-keys-plugin < 4.16.0
Obsoletes:	xfce4-playercontrol-plugin < 4.16.0
Obsoletes:	xfce4-playercontrol-plugin-audacious < 4.16.0
Obsoletes:	xfce4-playercontrol-plugin-xmms < 4.16.0
Obsoletes:	xfce4-quicklauncher-plugin < 4.16.0
Obsoletes:	xfce4-radio-plugin < 4.16.0
Obsoletes:	xfce4-taskbar-plugin < 4.16.0
Obsoletes:	xfce4-trigger-launcher < 4.16.0
Obsoletes:	xfce4-windowck-plugin < 4.16.0
Obsoletes:	xfprint < 4.16.0
Obsoletes:	xfprint-cups < 4.16.0
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
Requires:	xfce4-screenshooter >= 1.9.8
Requires:	xfce4-taskmanager >= 1.4.0
Suggests:	catfish >= 1.4.9
Suggests:	gigolo >= 0.5.0
Suggests:	parole >= 4.15.0
Suggests:	xfdashboard >= 0.8.0
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
Requires:	xfce4-clipman-plugin >= 1.4.4
Requires:	xfce4-cpufreq-plugin >= 1.2.1
Requires:	xfce4-cpugraph-plugin >= 1.1.0
Requires:	xfce4-datetime-plugin >= 0.8.1
Requires:	xfce4-dict-plugin >= 0.8.4
Requires:	xfce4-diskperf-plugin >= 2.6.3
Requires:	xfce4-eyes-plugin >= 4.5.1
Requires:	xfce4-fsguard-plugin >= 1.1.2
Requires:	xfce4-genmon-plugin >= 4.1.0
Requires:	xfce4-indicator-plugin >= 2.3.4-3
Requires:	xfce4-mailwatch-plugin >= 1.3.0
Requires:	xfce4-mount-plugin >= 1.1.5
Requires:	xfce4-mpc-plugin >= 0.5.2
Requires:	xfce4-netload-plugin >= 1.3.2
Requires:	xfce4-notes-plugin >= 1.8.1-5
Requires:	xfce4-places-plugin >= 1.8.1
Requires:	xfce4-sensors-plugin >= 1.3.95
Requires:	xfce4-smartbookmark-plugin >= 0.5.2
Requires:	xfce4-statusnotifier-plugin >= 0.2.1
Requires:	xfce4-systemload-plugin >= 1.2.4
Requires:	xfce4-time-out-plugin >= 1.0.3
Requires:	xfce4-timer-plugin >= 1.7.0
Requires:	xfce4-verve-plugin >= 2.0.1
Requires:	xfce4-wavelan-plugin >= 0.6.2
Requires:	xfce4-weather-plugin >= 0.10.2
Requires:	xfce4-whiskermenu-plugin >= 2.3.3
Requires:	xfce4-xkb-plugin >= 0.8.2

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
