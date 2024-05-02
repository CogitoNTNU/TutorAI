import SideBarSection from "./SideBarSection";
import { useContext, useEffect, useState } from "react";
import FileUploadService from "../services/FileUploadService";
import { FlashcardsProps } from "../components/Flashcard";
import CreateFlashcards from "../services/CreateFlashcardsService";
import { UserContext } from "../App";
import { FlashcardsContext } from "../pages/FlashcardsPage";
import { CompendiumContext } from "../pages/CompendiumPage";
import { QuizContext } from "../pages/QuizPage";
import { FilesContext } from "../pages/ChatPage";
import AddIcon from '@mui/icons-material/Add';
import CloseIcon from '@mui/icons-material/Close';
import MenuIcon from '@mui/icons-material/Menu';
import React from "react";
import { createCompendium } from "../services/CompendiumService";
import { createQuiz } from "../services/QuizService";

const SideBar: React.FC = () => {
    const { user, setUser } = useContext(UserContext);
    const { activeSets, setActiveSets } = useContext(FlashcardsContext);
    const { activeCompendium, setActiveCompendium } = useContext(CompendiumContext);
    const { activeQuiz, setActiveQuiz } = useContext(QuizContext); 

    const { activeFiles, setActiveFiles } = useContext(FilesContext);
    const [visibleSidebar, setVisibleSidebar] = useState<boolean>(false);
    const [visibleNewSet, setVisibleNewSet] = useState<boolean>(false);
    const [visibleNewCompendium, setVisibleNewCompendium] = useState<boolean>(false);
    const [visibleNewQuiz, setVisibleNewQuiz] = useState<boolean>(false);

    const [files, setFiles] = useState<string[]>([]);
    const [newSetFile, setNewSetFile] = useState<string>('');

    const handleFileUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
        if (e.target.files && e.target.files[0]) {
            const file = e.target.files[0];

            // Convert file to a data URL for react-pdf
            const reader = new FileReader();
            reader.readAsDataURL(file);

            try {
                await FileUploadService(file);
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

    const handleNewCompendium = async (e: React.ChangeEvent<HTMLFormElement>) => {
        e.preventDefault();
        try {
            const response = await createCompendium({
                document: newSetFile,
                start: e.target.start.value,
                end: e.target.end.value,
            });

            console.log('Response: compendium', response);
            setActiveCompendium(response);
        }
        catch (error) {
            console.error('Error creating new compendium:', error);
        }
    }

    const handleNewQuiz = async (e: React.ChangeEvent<HTMLFormElement>) => {
        e.preventDefault();
        setVisibleNewQuiz(false);
        try {
            const response = await createQuiz({
                document: newSetFile,
                start: e.target.start.value,
                end: e.target.end.value,
            });
            setActiveQuiz(response);
            console.log('Response: quiz', response);
            
        }
        catch (error) {
            console.error('Error creating new quiz:', error);
        }
    }

    const handleSelectedSet = (e: React.ChangeEvent<HTMLInputElement>) => {
        const selectedSet = e.target.value;
        
        // Check if the name of the set is already in the active sets
        if (activeSets.find((set) => set.name === selectedSet)) {
            // If it is, remove it from the active sets
            const newActiveSets = activeSets.filter((set) => set.name !== selectedSet);
            setActiveSets(newActiveSets);
            return;
        } else {
            const set = user.sets.find((set) => set.name === selectedSet);
            if (!set) {
                return;
            }
            // If it's not, add it to the active sets
            setActiveSets([...activeSets, set]);
        }
    }

    const handleSelectedFile = (e: React.ChangeEvent<HTMLInputElement>) => {
        const selectedFile = e.target.value;

        // Check if the name of the file is already in the active files
        if (activeFiles.find((file) => file === selectedFile)) {
            // If it is, remove it from the active files
            const newActiveFiles = activeFiles.filter((file) => file !== selectedFile);
            setActiveFiles(newActiveFiles);
            return;
        } else {
            // If it's not, add it to the active files
            setActiveFiles([...activeFiles, selectedFile]);
        }
    }

    useEffect(() => {
        setFiles(['Cogito.pdf']);
    }, []);

    return (
        <>
            <div className='absolute w-64'>
                {!visibleSidebar && (
                <button className='text-black px-4 py-2 rounded' onClick={() => setVisibleSidebar(true)}>
                    <MenuIcon fill='none' />
                </button>
                )}
                
                {visibleSidebar && (
                <div className={`z-10 bg-blue-200 w-full h-full  ${visibleSidebar ? '' : 'hidden'}`}>
                    <div className='p-2 w-full bg-blue-300 flex justify-between items-center'>
                        <h1 className='font-semibold'>Select</h1>
                        <button className='' onClick={() => setVisibleSidebar(false)}>
                            <CloseIcon />
                        </button>
                    </div>

                    <SideBarSection className='' title='Files'>
                        <div className="flex flex-col">
                            {files.map((file, index) => (
                            <label key={index} className='m-2 pl-10 w-full flex justify-left items-center text-left'>
                                <input className='w-5 h-5' type='checkbox' name='selectedFile' value={file} onChange={(e) => handleSelectedFile(e)} />
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
                    <SideBarSection className='' title='Compendium'>
                        {[<button className='pl-10 w-full text-left' onClick={() => setVisibleNewCompendium(true)}>+ New Compendium...</button>]}
                    </SideBarSection>
                    <SideBarSection className='' title='Quiz'>
                        {[<button className='pl-10 w-full text-left' onClick={() => setVisibleNewQuiz(true)}>+ New Quiz...</button>]}
                    </SideBarSection>
                </div>
                )}
            </div>

            {visibleNewSet && (
            <form className='absolute z-10 top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 flex flex-col justify-between p-5 bg-white p-4 w-96 h-72 rounded-lg shadow-lg' onSubmit={handleNewSet}> {/* TODO: check if translate tailwind works, or if it should be -translate-x-1/2 */}
                <div className='w-full flex justify-between items-center'>
                    <h1 className='font-bold'>New Set</h1>
                    <button className='' onClick={() => setVisibleNewSet(false)}>
                        <CloseIcon />
                    </button>
                </div>
                <input className='' name='setname' type='text' placeholder='Set name...' />
                <label className='font-semibold'>Select a file:</label>
                <ul>
                    {files.length === 0 && (
                    <li className='pl-2 w-full text-left'>
                        <p>No files uploaded yet.</p>
                    </li>
                    )}
                    {files.map((file, index) => (
                    <li key={index} className='pl-10 w-full text-left'>
                        <label>
                            <input type='radio' name='selectedFile' value={file} onChange={(e) => setNewSetFile(e.target.value)} />
                            {file}
                        </label>
                    </li>
                    ))}
                </ul>
                <label className='font-semibold'>Select a range:</label>
                <div className='flex justify-between items-center w-full'>
                    <input className='' name='start' type='number' placeholder='Start page...' />
                    <input className='' name='end' type='number' placeholder='End page...' />
                </div>
                <button className='w-full bg-blue-100 hover:bg-blue-300' type='submit'>Create</button>
            </form>
            )}

            {visibleNewCompendium && (
            <form className='absolute z-10 top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 flex flex-col justify-between p-5 bg-white p-4 w-96 h-72 rounded-lg shadow-lg' onSubmit={handleNewCompendium}> {/* TODO: check if translate tailwind works, or if it should be -translate-x-1/2 */}
                <div className='w-full flex justify-between items-center'>
                    <h1 className='font-bold'>New Compendium</h1>
                    <button className='' onClick={() => setVisibleNewCompendium(false)}>
                        <CloseIcon />
                    </button>
                </div>
                <input className='' name='setname' type='text' placeholder='Set name...' />
                <label className='font-semibold'>Select a file:</label>
                <ul>
                    {files.length === 0 && (
                    <li className='pl-2 w-full text-left'>
                        <p>No files uploaded yet.</p>
                    </li>
                    )}
                    {files.map((file, index) => (
                    <li key={index} className='pl-10 w-full text-left'>
                        <label>
                            <input type='radio' name='selectedFile' value={file} onChange={(e) => setNewSetFile(e.target.value)} />
                            {file}
                        </label>
                    </li>
                    ))}
                </ul>
                <label className='font-semibold'>Select a range:</label>
                <div className='flex justify-between items-center w-full'>
                    <input className='' name='start' type='number' placeholder='Start page...' />
                    <input className='' name='end' type='number' placeholder='End page...' />
                </div>
                <button className='w-full bg-blue-100 hover:bg-blue-300' type='submit'>Create</button>
            </form>
            )}

            {visibleNewQuiz && (<form className='absolute z-10 top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 flex flex-col justify-between p-5 bg-white p-4 w-96 h-72 rounded-lg shadow-lg' onSubmit={handleNewQuiz}> {/* TODO: check if translate tailwind works, or if it should be -translate-x-1/2 */}
                <div className='w-full flex justify-between items-center'>
                    <h1 className='font-bold'>New Quiz</h1>
                    <button className='' onClick={() => setVisibleNewQuiz(false)}>
                        <CloseIcon />
                    </button>
                </div>
                <input className='' name='setname' type='text' placeholder='Set name...' />
                <label className='font-semibold'>Select a file:</label>
                <ul>
                    {files.length === 0 && (
                    <li className='pl-2 w-full text-left'>
                        <p>No files uploaded yet.</p>
                    </li>
                    )}
                    {files.map((file, index) => (
                    <li key={index} className='pl-10 w-full text-left'>
                        <label>
                            <input type='radio' name='selectedFile' value={file} onChange={(e) => setNewSetFile(e.target.value)} />
                            {file}
                        </label>
                    </li>
                    ))}
                </ul>
                <label className='font-semibold'>Select a range:</label>
                <div className='flex justify-between items-center w-full'>
                    <input className='' name='start' type='number' placeholder='Start page...' />
                    <input className='' name='end' type='number' placeholder='End page...' />

                </div>
                <button className='w-full bg-blue-100 hover:bg-blue-300' type='submit'>Create</button>
            </form>)}

        </>
    )

    
};

export default SideBar;