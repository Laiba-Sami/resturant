import ErrorHandler from "../error/error.js";
import { Reservation } from "../models/reservationSchema.js";

export const sendReservation = async (req, res, next) => {
    const { firstName, lastName, email, phone, date, time } = req.body;

    // Validate required fields
    if (!firstName || !lastName || !email || !phone || !date || !time) {
        return next(new ErrorHandler("Please fill the full Reservation Form", 400));
    }

    try {
        // Pass the fields as an object
        await Reservation.create({
            firstName,
            lastName,
            email,
            phone,
            date,
            time,
        });

        // Send success response
        res.status(200).json({
            success: true,
            message: "Reservation sent successfully!",
        });
    } catch (error) {
        // Handle validation errors
        if (error.name === "ValidationError") {
            const validationErrors = Object.values(error.errors).map((err) => err.message); // Fixed typo: 'erros' -> 'errors'
            return next(new ErrorHandler(validationErrors.join(", "), 400));
        }

        // Handle other errors
        return next(error);
    }
};



