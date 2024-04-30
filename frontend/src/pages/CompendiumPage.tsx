import { createContext, useState } from "react";
import { Compendium } from "../types/Compendium";
import SideBar from "../components/SideBar";

const CompendiumContext = createContext<{
    activeCompendium: Compendium | null,
    setActiveCompendium: (compendium: Compendium | null) => void;
}>({
    activeCompendium: null,
    setActiveCompendium: () => {}
});

const CompendiumPage: React.FC = () => {
    
    const [activeCompendium, setActiveCompendium] = useState<Compendium | null>(null);
    return (

        <div>
            <CompendiumContext.Provider value={{activeCompendium, setActiveCompendium}}>
                <SideBar />
                <div className="absolute left-1/2 transform -translate-x-1/2 w-2/5 h-full'">    
                    {!activeCompendium && (
                        <h1 className='text-m font-bold'>Select or create a compendium...</h1>
                    )}

                    {activeCompendium && (
                        <div>
                            <h1>{activeCompendium.document}</h1>
                            <p>{activeCompendium.summary}</p>
                            <p>Pages {activeCompendium.start} to {activeCompendium.end}</p>
                            {activeCompendium.key_concepts.map((concept) => (
                                <p key={concept}>{concept}</p>
                                ))}
                        </div>
                    )}
                </div>
            </CompendiumContext.Provider>
        </div>
    );
};

export default CompendiumPage;
export { CompendiumContext }