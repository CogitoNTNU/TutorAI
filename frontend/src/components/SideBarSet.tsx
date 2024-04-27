const SideBarSet: React.FC<{ name: string }> = ({ name }) => {

    return (
        <div className='pl-10'>
            <button>{name}</button>
        </div>
    )
};

export default SideBarSet;