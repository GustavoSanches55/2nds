import React from "react";
import {HeadProvider, Link, Title} from 'react-head';

const headTags = [];

const Head = () => {
    return (
        <HeadProvider>
            <div>
                <title>S.I.L.V.I.A</title>
                <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
            </div>
        </HeadProvider>

    );
};

export default Head;

