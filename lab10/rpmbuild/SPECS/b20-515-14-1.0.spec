Name:          b20-515-14
Version:       1.0
Release:       1%{?dist}
Summary:       Программа студента Соколовского Степана группы Б20-515
Group:         Testing
License:       GPL
URL:           https://github.com/StephanSok
Source0:       %{name}-%{version}.tar.gz
BuildRequires: /bin/rm, /bin/mkdir, /bin/cp
Requires:      /bin/bash, /usr/bin/date
BuildArch:     noarch

%description
A test package

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 b20-515-14 %{buildroot}%{_bindir}
sudo yum install gnuplot

%files
%{_bindir}/b20-515-14

%changelog
* Thu Oct 16 2012 Sokolovskii
- Added %{_bindir}/b20-515-14

