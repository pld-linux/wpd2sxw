Summary:	Converting WordPerfect(TM) documents into OpenOffice.org Writer format
Summary(pl):	Konwersja dokumentów WordPerfecta(TM) na format OpenOffice.org Writera
Name:		wpd2sxw
Version:	0.6.0
Release:	1
License:	LGPL
Group:		Applications/Publishing
Source0:	http://dl.sourceforge.net/libwpd/%{name}-%{version}.tar.gz
# Source0-md5:	8447e89c580d302e5b13e6eb6064a2ab
URL:		http://libwpd.sourceforge.net/
BuildRequires:	libwpd-devel >= 0.7.0
BuildRequires:	pkgconfig
Requires:	libwpd >= 0.7.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool for converting WordPerfect documents into OpenOffice.org Writer
format.

%description -l pl
Narzêdzie do konwertowania dokumentów WordPerfecta do formatu
OpenOffice.org Writera.

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
%doc CHANGES README
%attr(755,root,root) %{_bindir}/*
