%global gemname childprocess

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: A simple and reliable gem for controlling external programs
Name: rubygem-%{gemname}
Version: 0.2.0
Release: 2%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/jarib/childprocess
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby
Requires: rubygem(ffi) => 1.0.6
Requires: rubygem(ffi) < 1.1
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
This gem aims at being a simple and reliable solution for controlling external
programs running in the background on any Ruby / OS combination.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gemdir}
gem install --local --install-dir .%{gemdir} --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -a .%{gemdir}/* %{buildroot}%{gemdir}/
rm -f %{buildroot}%{geminstdir}/.document %{buildroot}%{geminstdir}/.gitignore
rm -f %{buildroot}%{geminstdir}/.rspec %{buildroot}%{geminstdir}/Rakefile
rm -f %{buildroot}%{geminstdir}/childprocess.gemspec
rm -f %{buildroot}%{geminstdir}/Gemfile
chmod 644 %{buildroot}%{geminstdir}/lib/childprocess/jruby/process.rb
chmod 644 %{buildroot}%{geminstdir}/lib/childprocess/windows/process.rb
chmod 644 %{buildroot}%{geminstdir}/spec/*.rb


%files
%dir %{geminstdir}
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/README.md
%{geminstdir}/lib
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/spec


%changelog
* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 03 2011 Chris Lalancette <clalance@redhat.com> - 0.2.0-1
- Initial package
