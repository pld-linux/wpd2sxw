# NOTE: obsoleted by writerperfect.spec
Summary:	Converting WordPerfect(TM) documents into OpenOffice.org Writer format
Summary(pl.UTF-8):	Konwersja dokumentów WordPerfecta(TM) na format OpenOffice.org Writera
Name:		wpd2sxw
Version:	0.8.0
Release:	1.1
License:	GPL v2
Group:		Applications/Publishing
Source0:	http://downloads.sourceforge.net/libwpd/writerperfect-%{version}.tar.gz
# Source0-md5:	d0255522926690cfa82a425016da4f80
URL:		http://libwpd.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRequires:	libwpd-devel >= 0.9.0
BuildRequires:	libwpg-devel >= 0.2.0
BuildRequires:	pkgconfig
Requires:	libwpd >= 0.9.0
Requires:	libwpg >= 0.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool for converting WordPerfect documents into OpenOffice.org Writer
format.

%description -l pl.UTF-8
Narzędzie do konwertowania dokumentów WordPerfecta do formatu
OpenOffice.org Writera.

%prep
%setup -q -n writerperfect-%{version}

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
%doc NEWS README
%attr(755,root,root) %{_bindir}/wpd2odt
%attr(755,root,root) %{_bindir}/wpg2odg
