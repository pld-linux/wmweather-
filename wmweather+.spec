Summary:	Applet that displays the weather
Summary(pl):	Aplet wy¶wietlaj±cy informacje o pogodzie
Name:		wmweather+
Version:	2.9
Release:	0.1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://dl.sourceforge.net/wmweatherplus/%{name}-%{version}.tar.gz
# Source0-md5:	ede58d7ed589d5c41b9b68a2703a8f7d
Source1:	%{name}.desktop
URL:		http://www.sourceforge.net/projects/wmweahterplus/
BuildRequires:	w3c-libwww-devel
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmweather+ will download the National Weather Service METAR bulletins;
AVN, ETA, and MRF forecasts; and any weather map for display in a
WindowMaker dockapp. Think wmweather with a smaller font, forecasts, a
weather map, and a sky condition display.

%description -l pl
wmweather+ ¶ci±ga biuletyny METAR z National Weather Service, prognozy
AVN, ETA i MRF oraz dowolne mapy pogody do wy¶wietlania w dockappie
WindowMakera. Ten program mo¿na sobie wyobraziæ jako wmweather z
mniejszym fontem, prognozami, map± pogody i wy¶wietlaniem stanu nieba.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog HINTS README
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_desktopdir}/*
