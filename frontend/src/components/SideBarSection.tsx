import KeyboardArrowLeftIcon from '@mui/icons-material/KeyboardArrowLeft';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import { useState } from 'react';

const SideBarSection: React.FC<{ className: string, title: string, children: React.ReactNode[] }> = ({ className, title, children }) => {
    const [visibleSection, setVisibleSection] = useState<boolean>(false);

    return (
        <div className={'w-full' + ' ' + className}>
            <div className='py-1 pl-8 w-full bg-blue-300 hover:bg-blue-400 hover:cursor-pointer flex justify-between items-center' onClick={() => setVisibleSection(!visibleSection)}>
                <h2 className=''>{title}</h2>
                {visibleSection ? <KeyboardArrowDownIcon /> : <KeyboardArrowLeftIcon />}
            </div>
            {visibleSection && children}
        </div>
    );
};

export default SideBarSection;