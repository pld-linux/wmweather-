Summary:	Applet that displays the weather
Summary(pl):	Aplet wy¶wietlaj±cy informacje o pogodzie
Name:		wmweather+
Version:	2.5
Release:	0.1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://dl.sourceforge.net/wmweatherplus/%{name}-%{version}.tar.gz
# Source0-md5:	32d16bea88cf374964b5e87a15698c8d
Source1:	%{name}.desktop
URL:		http://www.sourceforge.net/projects/wmweahterplus/
BuildRequires:	w3c-libwww-devel
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmweather+ will download the National Weather Serivce METAR bulletins;
AVN, ETA, and MRF forecasts; and any weather map for display in a
WindowMaker dockapp. Think wmweather with a smaller font, forecasts, a
weather map, and a sky condition display.

#%description -l pl

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog HINTS README
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
