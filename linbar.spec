Summary:	LinBar
Summary(pl):	LinBar
Name:		linbar
Version:	0.4
Release:	1
License:	GPL
Group:		System
######		Unknown group!
#Group(pl):	
Source0:	ftp://argeas.cs-net.gr/pub/unix/linux/linbar/%{name}-%{version}.tar.gz
Patch0:		
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q

%build
#./configure --prefix=%{_prefix}
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
make prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/%name-%version

%files
%defattr(644,root,root,755)
%doc
#%attr(,,)
