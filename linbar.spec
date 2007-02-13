Summary:	LinBar - Linux Barcode support
Summary(pl.UTF-8):	LinBar - obsługa czytników kodów paskowych dla Linuksa
Name:		linbar
Version:	0.5
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://argeas.cs-net.gr/pub/unix/linux/linbar/%{name}-%{version}.tar.gz
# Source0-md5:	c835d07912b3ee84241530f68923e8ee
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The linbar utility reads from a specified serial port and puts the
characters to the current console keyboard buffer. It's primary usage
is for serial barcode readers. As far as I know, it works only on
Linux console.

%description -l pl.UTF-8
Program linbar czyta z zadanego portu szeregowego i odczytane znaki
wrzuca do bufora klawiatury aktualnej konsoli. Głównym zastosowaniem
jest obsługa czytników kodów paskowych. Jak na razie działa tylko z
konsolą Linuksa.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cxx}" \
	OPTIMIZE="%{rpmcflags} -Wall" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install linbar $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS README INSTALL TODO
%attr(755,root,root) %{_bindir}/linbar
