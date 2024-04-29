import KeyboardArrowLeftIcon from '@mui/icons-material/KeyboardArrowLeft';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import { useState } from 'react';

const SideBarSection: React.FC<{ className: string, title: string, children: React.ReactNode[] }> = ({ className, title, children }) => {
    const [visibleSection, setVisibleSection] = useState<boolean>(false);

    return (
        <div className={'w-full' + ' ' + className}>
            <div className='pl-8 w-full bg-blue-300 flex justify-between items-center'>
                <h2 className=''>{title}</h2>
                <button className='' onClick={() => setVisibleSection(!visibleSection)}>
                    {visibleSection ? <KeyboardArrowDownIcon /> : <KeyboardArrowLeftIcon />}
                </button>
            </div>
            {visibleSection && children}
        </div>
    );
};

export default SideBarSection;