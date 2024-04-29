import SideBarSection from "./SideBarSection";
import { useContext, useState } from "react";
import FileUploadService from "../services/FileUploadService";
import { FlashcardsProps } from "../components/Flashcard";
import CreateFlashcards from "../services/CreateFlashcardsService";
import { UserContext } from "../App";

const SideBar: React.FC = () => {
    const { user, setUser } = useContext(UserContext);
    const [visibleSidebar, setVisibleSidebar] = useState<boolean>(true);
    const [visibleNewSet, setVisibleNewSet] = useState<boolean>(false);
    const [files, setFiles] = useState<string[]>([]);
    const [newSetFile, setNewSetFile] = useState<string>('');

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

    const handleNewSet = async (e: React.ChangeEvent<HTMLFormElement>) => {
        e.preventDefault();

        try {
            const response = await CreateFlashcards(newSetFile, e.target.start.value, e.target.end.value);
            
            const flashcards: FlashcardsProps = {
                name: e.target.setname.value,
                flashcards: response.data.flashcards
            };

            console.log('Response:', response);
            // Update the context with the new set
            setUser({...user, sets: [...user.sets, flashcards]});
            setVisibleNewSet(false);
        } catch (error) {
            console.error('Error creating new set:', error);
        }
    }

    return (
        <>
            {!visibleSidebar && (
            <button className='bg-blue-500 text-white px-4 py-2 rounded' onClick={() => setVisibleSidebar(true)}>Open Sidebar</button>
            )}
            
            {visibleSidebar && (
            <div className={`bg-blue-200 w-1/5 ${visibleSidebar ? '' : 'hidden'}`}>
                <div className='p-2 w-full bg-blue-300 flex justify-between items-center'>
                    <h1 className=''>SideBar</h1>
                    <button className='' onClick={() => setVisibleSidebar(false)}>Close Sidebar</button>
                </div>
                <SideBarSection className='' title='Files'>
                    {files.map((file, index) => (
                        <label key={index} className='pl-10 w-full text-left'>
                            <input type='radio' name='selectedFile' value={file} onChange={(e) => setNewSetFile(e.target.value)} />
                            {file}
                        </label>
                    ))}

                    <input className='' type='file' accept='.pdf' onChange={handleFileUpload} />
                </SideBarSection>
                <SideBarSection className='' title="Sets">
                    {user?.sets.map((set: FlashcardsProps, index) => (
                        <div key={index} className='pl-10'>
                            <button>{set.name}</button>
                        </div>
                    ))}

                    <button className='pl-10 w-full text-left' onClick={() => setVisibleNewSet(true)}>+ New set...</button>
                </SideBarSection>
            </div>
            )}

            {visibleNewSet && (
            <form className='absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-white p-4 rounded-lg shadow-lg' onSubmit={handleNewSet}>
                <input className='' name='setname' type='text' placeholder='Set name...' />
                <ul>
                    {files.map((file, index) => (
                    <li key={index} className='pl-10 w-full text-left'>
                        <label>
                            <input type='radio' name='selectedFile' value={file} onChange={(e) => setNewSetFile(e.target.value)} />
                            {file}
                        </label>
                    </li>
                    ))}
                </ul>
                <input className='' name='start' type='number' placeholder='Start page...' />
                <input className='' name='end' type='number' placeholder='End page...' />
                <button className='' type='submit'>Create</button>
            </form>
            )}
        </>
    )
};

export default SideBar;