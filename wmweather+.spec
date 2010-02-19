Summary:	Applet that displays the weather
Summary(pl.UTF-8):	Aplet wyświetlający informacje o pogodzie
Name:		wmweather+
Version:	2.9
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://dl.sourceforge.net/wmweatherplus/%{name}-%{version}.tar.gz
# Source0-md5:	ede58d7ed589d5c41b9b68a2703a8f7d
Source1:	%{name}.desktop
URL:		http://www.sourceforge.net/projects/wmweatherplus/
BuildRequires:	XFree86-devel
BuildRequires:	pcre-devel
BuildRequires:	w3c-libwww-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmweather+ will download the National Weather Service METAR bulletins;
AVN, ETA, and MRF forecasts; and any weather map for display in a
WindowMaker dockapp. Think wmweather with a smaller font, forecasts, a
weather map, and a sky condition display.

%description -l pl.UTF-8
wmweather+ ściąga biuletyny METAR z National Weather Service, prognozy
AVN, ETA i MRF oraz dowolne mapy pogody do wyświetlania w dockappie
WindowMakera. Ten program można sobie wyobrazić jako wmweather z
mniejszym fontem, prognozami, mapą pogody i wyświetlaniem stanu nieba.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}/docklets

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog HINTS README
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_desktopdir}/docklets/*
