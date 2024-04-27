const SideBarSection: React.FC<{ className: string, title: string, children: React.ReactNode[] }> = ({ className, title, children }) => {
    return (
        <div className={'w-full' + ' ' + className}>
            <h2 className={'pl-8'}>{title}</h2>
            {children}
        </div>
    );
};

export default SideBarSection;