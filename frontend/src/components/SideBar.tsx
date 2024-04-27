import SideBarSection from "./SideBarSection";
import SideBarFile from "./SideBarFile";
import SideBarSet from "./SideBarSet";
import { useState } from "react";
import FileUploadService from "../services/FileUploadService";

const SideBar: React.FC = () => {
    const [visible, setVisible] = useState<boolean>(true);
    const [files, setFiles] = useState<string[]>([]);

    const handleFileUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
        if (e.target.files && e.target.files[0]) {
            const file = e.target.files[0];

            // Convert file to a data URL for react-pdf
            const reader = new FileReader();
            reader.onload = (e) => console.log(e.target?.result);
            reader.readAsDataURL(file);

            try {
                const response = await FileUploadService(file);
                console.log('Response:', response);
                setFiles([...files, file.name]);

                // Clear the input field
                e.target.value = '';
            } catch (error) {
                console.error('Error uploading file:', error);
            }
        }
    }

    return (
        <>
            {!visible && (
            <button className='bg-blue-500 text-white px-4 py-2 rounded' onClick={() => setVisible(true)}>Open Sidebar</button>
            )}
            
            {visible && (
            <div className={`bg-blue-200 w-1/5 ${visible ? '' : 'hidden'}`}>
                <div className='p-2 w-full bg-blue-300 flex justify-between items-center'>
                    <h1 className=''>SideBar</h1>
                    <button className='' onClick={() => setVisible(false)}>Close Sidebar</button>
                </div>
                <SideBarSection className='' title='Files'>
                    {files.map((file, index) => (
                        <SideBarFile key={index} name={file} />
                    ))}
                </SideBarSection>
                <SideBarSection className='' title="Sets">
                    <SideBarSet name='set1' />
                    <SideBarSet name='set2' />
                </SideBarSection>

                <input className='' type='file' accept='.pdf' onChange={handleFileUpload} />
            </div>
            )}
        </>
    )
};

export default SideBar;