export class Category{
    id: number;
    title: string;
}

export class Brand{
    id: number;
    title: string;
}

export class Product{
    id: number;
    title: string;
    image: string;
    description: string;
    ingredients: string;
    price: number;
    brand: number;
    category: number;
    barcode: number;
    quantity: number;
}

export class LoginResponse {
    token: string;
}
