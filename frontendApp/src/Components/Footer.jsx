import React from "react";

const Footer = () => {
  return (
    <footer className="bg-gray-900 text-gray-200 py-8 mt-12">
      <div className="container mx-auto px-4 flex flex-col md:flex-row items-center justify-between">
        {/* Logo/Title */}
        <div className="mb-4 md:mb-0 flex items-center">
          <span className="text-xl font-bold text-white">NoWasteWater2030</span>
        </div>
        {/* Navigation Links */}
        <nav className="mb-4 md:mb-0">
          <ul className="flex space-x-6">
            <li><a href="#about" className="hover:text-teal-400 transition">Visit my site: aarav.jain</a></li>
          </ul>
        </nav>
        <div className="text-sm text-gray-400">
          &copy; {new Date().getFullYear()} NoWasteWater2030. All rights reserved.
        </div>
      </div>
    </footer>
  );
};

export default Footer;
