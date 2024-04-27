const SideBarFile: React.FC<{ name: string }> = ({ name }) => {

    return (
        <button className='pl-10 w-full text-left'>{name}</button>
    )
};

export default SideBarFile;