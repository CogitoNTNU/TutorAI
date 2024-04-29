import SideBarSection from "./SideBarSection";
import { useContext, useState } from "react";
import FileUploadService from "../services/FileUploadService";
import { FlashcardsProps } from "../components/Flashcard";
import CreateFlashcards from "../services/CreateFlashcardsService";
import { UserContext } from "../App";
import { FlashcardsContext } from "../pages/FlashcardsPage";
import AddIcon from '@mui/icons-material/Add';
import CloseIcon from '@mui/icons-material/Close';
import MenuIcon from '@mui/icons-material/Menu';
import React from "react";

const SideBar: React.FC = () => {
    const { user, setUser } = useContext(UserContext);
    const { activeSets, setActiveSets } = useContext(FlashcardsContext);
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

    const fileInputRef = React.useRef<HTMLInputElement>(null);

    // Function to simulate clicking on the actual file input
    const handleButtonClick = () => {
        if (fileInputRef.current) {
            fileInputRef.current.click();
        }
    };

    const handleNewSet = async (e: React.ChangeEvent<HTMLFormElement>) => {
        e.preventDefault();

        try {
            const response = await CreateFlashcards(newSetFile, e.target.start.value, e.target.end.value);
            
            const flashcards: FlashcardsProps = {
                name: e.target.setname.value,
                flashcards: response.flashcards
            };

            console.log('Response:', response);
            // Update the context with the new set
            setUser({...user, sets: [...user.sets, flashcards]});
            setVisibleNewSet(false);
        } catch (error) {
            console.error('Error creating new set:', error);
        }
    }

    const handleSelectedSet = (e: React.ChangeEvent<HTMLInputElement>) => {
        const selectedSet = e.target.value;
        console.log('Selected set:', selectedSet)
        
        // Check if the name of the set is already in the active sets
        if (activeSets.find((set) => set.name === selectedSet)) {
            // If it is, remove it from the active sets
            const newActiveSets = activeSets.filter((set) => set.name !== selectedSet);
            console.log('New active sets:', newActiveSets);
            setActiveSets(newActiveSets);
            console.log('Active sets:', activeSets);
            return;
        } else {
            const set = user.sets.find((set) => set.name === selectedSet);
            console.log('Found set:', set);
            if (!set) {
                console.error('Set not found:', selectedSet);
                return;
            }
            // If it's not, add it to the active sets
            setActiveSets([...activeSets, set]);
            console.log('Active sets:', activeSets);
        }
    }

    return (
        <div className='absolute w-64'>
            {!visibleSidebar && (
            <button className='text-black px-4 py-2 rounded' onClick={() => setVisibleSidebar(true)}>
                <MenuIcon fill='none' />
            </button>
            )}
            
            {visibleSidebar && (
            <div className={`bg-blue-200 w-full ${visibleSidebar ? '' : 'hidden'}`}>
                <div className='p-2 w-full bg-blue-300 flex justify-between items-center'>
                    <h1 className=''>SideBar</h1>
                    <button className='' onClick={() => setVisibleSidebar(false)}>
                        <CloseIcon />
                    </button>
                </div>
                <SideBarSection className='' title='Files'>
                    <div className="flex flex-col">
                            {/* <label className='m-2 pl-10 w-full flex justify-left items-center text-left'>
                                <input className='w-5 h-5' type='checkbox' name='selectedFile' onChange={(e) => setNewSetFile(e.target.value)} />
                                <p className='w-4/5 pl-2 select-none overflow-hidden'>Sample filezzzzzzzzzzzzzzzzzzzzzzzzzzzzzz</p>
                            </label> */}
                        {files.map((file, index) => (
                            <label key={index} className='m-2 pl-10 w-full flex justify-left items-center text-left'>
                                {/* <input className='w-5 h-5' type='checkbox' name='selectedFile' value={file} onChange={(e) => setNewSetFile(e.target.value)} /> */}
                                <p className='w-4/5 pl-2 select-none overflow-hidden'>{file}</p>
                            </label>
                        ))}
                    </div>
                    <div className='relative'>
                        {/* Hidden file input */}
                        <input className="hidden" ref={fileInputRef} type="file" accept=".pdf" onChange={handleFileUpload} />

                        {/* Visible button */}
                        <button className="ml-auto mr-2 my-2 flex items-center justify-center w-8 h-8 rounded-full bg-blue-500 hover:bg-blue-600 text-white" onClick={handleButtonClick} aria-label="Add new file">
                            <AddIcon />
                        </button>
                    </div>
                </SideBarSection>
                <SideBarSection className='' title="Sets">
                    {user?.sets.map((set: FlashcardsProps, index) => (
                    <label className='m-2 pl-10 w-full flex justify-left items-center text-left' key={index}>
                        <input className='w-5 h-5' type='checkbox' name='selectedFile' value={set.name} onChange={(e) => handleSelectedSet(e)} />
                        <p className='w-4/5 pl-2 select-none overflow-hidden'>{set.name}</p>
                    </label>
                    ))}
                    <button className='pl-10 w-full text-left' onClick={() => setVisibleNewSet(true)}>+ New set...</button>
                </SideBarSection>
            </div>
            )}

            {visibleNewSet && (
            <form className='absolute top-1/2 left-1/2 transform -translate-1/2 bg-white p-4 rounded-lg shadow-lg' onSubmit={handleNewSet}>
                <div className='p-2 w-full bg-blue-300 flex justify-between items-center'>
                    <input className='' name='setname' type='text' placeholder='Set name...' />
                    <button className='' onClick={() => setVisibleNewSet(false)}>
                        <CloseIcon />
                    </button>
                </div>
                <label className=''>Select a file:</label>
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
        </div>
    )
};

export default SideBar;