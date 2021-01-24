let
  pkgs = import <nixpkgs> {};
  pythonPackages = pkgs.python3Packages;
in pythonPackages.buildPythonPackage rec {
  name = "mailserver";
  src = ./.;
  nativeBuildInputs = [
    pythonPackages.salmon-mail
  ];
  propagatedBuildInputs = [
    pythonPackages.salmon-mail
  ];
}
