%define		ecore_ver	1.7.0
%define		edje_ver	1.7.0
%define		eina_ver	1.7.0
%define		elementary_ver	1.7.0
%define		etrophy_ver	0.5.1
%define		evas_ver	1.7.0

Summary:	Elemines - EFL minesweeper clone
Summary(pl.UTF-8):	Elemines - klon sapera oparty na EFL
Name:		elemines
Version:	0.2.3
Release:	2
License:	BSD-like (code), GPL v2+ (some artwork) and SIL OFL (fonts)
Group:		Libraries
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	61851b2de5c2aef3fe41381bc2c444ed
URL:		http://enlightenment.org/
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake >= 1:1.10
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	libtool >= 2:2.2
BuildRequires:	ecore-devel >= %{ecore_ver}
BuildRequires:	edje >= %{edje_ver}
BuildRequires:	edje-devel >= %{edje_ver}
BuildRequires:	eina-devel >= %{eina_ver}
BuildRequires:	elementary-devel >= %{elementary_ver}
BuildRequires:	etrophy-devel >= %{etrophy_ver}
BuildRequires:	evas-devel >= %{evas_ver}
BuildRequires:	pkgconfig
Requires:	ecore >= %{ecore_ver}
Requires:	edje-libs >= %{edje_ver}
Requires:	eina >= %{eina_ver}
Requires:	elementary >= %{elementary_ver}
Requires:	etrophy >= %{etrophy_ver}
Requires:	evas >= %{evas_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Elemines is an EFL minesweeper clone.

%description -l pl.UTF-8
Elemines to klon gry w sapera oparty na bibliotekach EFL.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	icondir=%{_pixmapsdir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/eleminesql.la
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/elemines

%{__mv} $RPM_BUILD_ROOT%{_localedir}/pt{_PT,}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS OFL.txt README README.artwork TODO
%attr(755,root,root) %{_bindir}/elemines
%attr(755,root,root) %{_bindir}/eleminesql
%attr(755,root,root) %{_libdir}/eleminesql.so
%{_datadir}/%{name}
%{_desktopdir}/elemines.desktop
%{_pixmapsdir}/elemines.png
%{_mandir}/man1/elemines.1*
