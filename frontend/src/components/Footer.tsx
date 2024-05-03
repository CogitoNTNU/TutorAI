import { FaFacebookF, FaInstagram, FaLinkedinIn, FaGithub} from 'react-icons/fa';

const Footer = () => {
  return (
    <footer className="bg-teal-800 text-white flex items-center justify-between p-4 text-sm">
      <div>
        <p>Cogito NTNU © 2024</p>
        <p>Org.Nr: 920 628 788</p>
      </div>
      <div className="flex">
        <a href="https://www.facebook.com/CogitoNTNU" target="_blank" rel="noopener noreferrer" className="mr-2">
          <FaFacebookF />
        </a>
        <a href="https://www.instagram.com/cogitontnu/" target="_blank" rel="noopener noreferrer" className="mr-2">
          <FaInstagram />
        </a>
        <a href="https://www.linkedin.com/company/cogito-ntnu/" target="_blank" rel="noopener noreferrer" className="mr-2">
          <FaLinkedinIn />
        </a>
        <a href='https://github.com/CogitoNTNU' target='_blank' rel='noopener noreferrer' className='ml-2'>
            <FaGithub />
        </a>
      </div>
    </footer>
  );
};

export default Footer;